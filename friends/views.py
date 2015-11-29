from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from friends.models import Friend
from friends.serializers import FriendSerializer


@api_view(['GET', 'POST'])
@csrf_exempt
def start(request):
    from random import randint

    if request.method == 'GET':
        x = randint(0, 100)
        y = randint(0, 100)
        me = Friend(x=x, y=y, me=True)
        me.save()
        me_serialized = FriendSerializer(me)
        return Response(me_serialized.data)




