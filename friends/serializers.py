from rest_framework import serializers
from friends.models import Friend


class FriendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Friend
        fields = ('id', 'me', 'x', 'y')


    def update(self, inst, valid_data):
        x = valid_data.get('x', inst.x)
        y = valid_data.get('y', inst.y)
        min_pos, max_pos = Friend.world_size()
        inst.x = x if x <= max_pos and x >= min_pos else inst.x
        inst.y = y if y <= max_pos and y >= min_pos else inst.y
        inst.save()
        return inst


class FriendsSerializer(serializers.ModelSerializer):
    distance = serializers.FloatField(read_only=True)

    class Meta:
        model = Friend
        fields = ('id', 'x', 'y', 'distance')


    def update(self, inst, valid_data):
        x = valid_data.get('x', inst.x)
        y = valid_data.get('y', inst.y)
        min_pos, max_pos = Friend.world_size()
        inst.x = x if x <= max_pos and x >= min_pos else inst.x
        inst.y = y if y <= max_pos and y >= min_pos else inst.y
        inst.distance = Friend.objects.filter(
            me=True
        ).first().distance_from(inst.x, inst.y)
        inst.save()
        return inst


    def create(self, valid_data):
        x = valid_data.get('x')
        y = valid_data.get('y')
        if x is None or y is None:
            return None
        min_pos, max_pos = Friend.world_size()
        if x > max_pos or x < min_pos:
            return None
        if y > max_pos or y < min_pos:
            return None

        me = Friend.objects.filter(me=True).first()

        distance = me.distance_from(x, y)

        friend = Friend(x=x, y=y, distance=distance)

        me.add_friend(friend)

        return friend


class NearFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('id', 'distance',)


class RouteSerializer(serializers.ModelSerializer):
    route_from = serializers.SerializerMethodField()


    def get_route_from(self, obj):
        from django.db.models import Q

        to_id = self.context.get('friend_id')
        friends = Friend.objects.filter(
            Q(pk=obj.id) | Q(pk=to_id)
        ).all()
        friends_serialized = FriendSerializer(friends, many=True)
        return friends_serialized.data


    class Meta:
        model = Friend
        fields = ('route_from',)




