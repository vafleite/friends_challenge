from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from friends.models import Friend
from friends.serializers import FriendSerializer, NearFriendsSerializer


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
        me = self.get_me()
        near_num = self.kwargs.get('near_num', False)
        if near_num is not False and near_num.isnumeric():
            near_num = int(near_num)
            return me.friend_set.all().order_by('distance')[:near_num]
        else:
            return me.friend_set.all().order_by('distance')


    def get_me(self):
        me = Friend.objects.filter(me=True).first()
        if me:
            return me
        else:
            raise Http404




