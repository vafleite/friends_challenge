from rest_framework import serializers
from friends.models import Friend


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('id', 'me', 'x', 'y', 'friends_route')


    def update(self, inst, valid_data):
        x = valid_data.get('x', inst.x)
        y = valid_data.get('y', inst.y)
        min_pos, max_pos = Friend.world_size()
        inst.x = x if x <= max_pos and x >= min_pos else inst.x
        inst.y = y if y <= max_pos and y >= min_pos else inst.y
        inst.save()
        return inst


class NearFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('id', 'distance',)


