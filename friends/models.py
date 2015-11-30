from django.db import models


class Friend(models.Model):
    me = models.BooleanField(default=False)
    x = models.IntegerField()
    y = models.IntegerField()
    distance = models.FloatField(null=True)

    friends = models.ForeignKey('self', null=True, blank=True)


    @property
    def friends_route(self):
        friends = self.friend_set.all().order_by('distance')
        return [{'id': f.id, 'distance': f.distance} for f in friends]


    def add_friend(self, f):
        if self.friend_exists(f):
            return False
        else:
            f.save()
            self.friend_set.add(f)
            return True


    def friend_exists(self, f):
        if self.friend_set.filter(x=f.x).filter(
            y=f.y
        ).count() > 0:
            return True
        else:
            return False


    def generate_friends(self):
        from random import randint

        self.friend_set.clear()
        friends_num = randint(3, 10)

        for i in range(friends_num):
            while True:
                x = Friend.random_position()
                y = Friend.random_position()
                distance = self.distance_from(x, y)
                f = Friend(x=x, y=y, distance=distance)
                if self.add_friend(f):
                    break


    def randomize(self):
        self.x = Friend.random_position()
        self.y = Friend.random_position()
        self.save()

        for friend in self.friend_set.all():
            while True:
                friend.x = Friend.random_position()
                friend.y = Friend.random_position()
                friend.distance = self.distance_from(friend.x, friend.y)
                if not self.friend_exists(friend):
                    friend.save()
                    break


    def distance_from(self, friend_x, friend_y):
        import math

        dist = math.hypot(friend_x - self.x, friend_y - self.y)
        dist = round(dist, 2)

        return dist


    @staticmethod
    def random_position():
        from random import randint

        return randint(*Friend.world_size())


    @staticmethod
    def world_size():
        return (0, 100)


    def __str__(self):
        return '{0} -> x: {1}; y: {2}'.format(
            self.id, self.x, self.y
        )

