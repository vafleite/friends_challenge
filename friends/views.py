from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from friends.models import Friend
from friends.serializers import FriendSerializer
from friends.serializers import NearFriendsSerializer
from friends.serializers import FriendsSerializer
from friends.serializers import RouteSerializer


class Me(APIView):

    permission_classes = (AllowAny,)

    def get_or_create_object(self):
        me = Friend.objects.filter(me=True).first()
        if not me:
            x = Friend.random_position()
            y = Friend.random_position()
            me = Friend(x=x, y=y, me=True)
            me.save()
            me.generate_friends()

        return me


    def get_object(self):
        me = Friend.objects.filter(me=True).first()
        if me:
            return me
        else:
            raise Http404


    def get(self, request):
        me = self.get_or_create_object()
        me_serialized = FriendSerializer(me)
        return Response(me_serialized.data)


    def put(self, request):
        me = self.get_object()
        me_serialized = FriendSerializer(me, data=request.data)

        if me_serialized.is_valid():
            me_serialized.save()
            return Response(me_serialized.data)

        return Response(
            me_serialized.errors, status=status.HTTP_400_BAD_REQUEST
        )



class Reset(APIView):

    permission_classes = (AllowAny,)


    def get(self, request):
        Friend.objects.all().delete()

        x = Friend.random_position()
        y = Friend.random_position()
        me = Friend(x=x, y=y, me=True)
        me.save()
        me.generate_friends()

        me_serialized = FriendSerializer(me)

        return Response(me_serialized.data)


class Nearest(ListAPIView):

    permission_classes = (AllowAny,)
    serializer_class = NearFriendsSerializer


    def get_queryset(self):
        me = self.get_object()
        near_num = self.kwargs.get('near_num', False)
        if near_num is not False and near_num.isnumeric():
            near_num = int(near_num)
            return me.friend_set.all().order_by('distance')[:near_num]
        else:
            return me.friend_set.all().order_by('distance')[:3]


    def get_object(self):
        me = Friend.objects.filter(me=True).first()
        if me:
            return me
        else:
            raise Http404


class Friends(ListCreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = FriendsSerializer
    queryset = Friend.objects.filter(me=True).first().friend_set.all()


class FriendsDetails(RetrieveUpdateDestroyAPIView):

    permission_classes = (AllowAny,)
    serializer_class = FriendsSerializer
    queryset = Friend.objects.filter(me=True).first().friend_set.all()


class RouteTo(APIView):

    permission_classes = (AllowAny,)

    def get_object(self, from_id):
        try:
            return Friend.objects.get(pk=from_id)
        except Friend.DoesNotExist:
            raise Http404


    def get(self, request, to_id, from_id=None):
        if from_id is None:
            from_friend = Friend.objects.filter(me=True).first()
            if not from_friend:
                raise Http404
        else:
            from_friend = self.get_object(from_id)

        serializer = RouteSerializer(from_friend, context={'friend_id': to_id})

        return Response(serializer.data)



