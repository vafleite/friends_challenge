from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from friends.models import Friend
from friends.serializers import FriendSerializer


class Me(APIView):

    def get(self, request):
        if request.method == 'GET':
            me = Friend(me=True)
            me.save()
            me.generate_friends()
            me_serialized = FriendSerializer(me)
            return Response(me_serialized.data)




