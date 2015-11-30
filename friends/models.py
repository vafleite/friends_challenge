from django.db import models


class Friend(models.Model):
    me = models.BooleanField(default=False)
    x = models.IntegerField()
    y = models.IntegerField()

    friends = models.ForeignKey('self', null=True, blank=True)

    friends_route = []


    def save(self, *args, **kwargs):
        if self.me:
            self.x = self.world_size()
            self.y = self.world_size()

        super(Friend, self).save(*args, **kwargs)


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
        friends_num = randint(1, 10)

        for i in range(friends_num):
            while True:
                x = self.world_size()
                y = self.world_size()
                f = Friend(x=x, y=y)
                if self.add_friend(f):
                    break

        self.get_route()


    def randomize(self):
        self.x = self.world_size()
        self.y = self.world_size()
        self.save()

        for friend in self.friend_set.all():
            while True:
                friend.x = self.world_size()
                friend.y = self.world_size()
                if not self.friend_exists(friend):
                    friend.save()
                    break


    def get_route(self):
        from operator import itemgetter

        friends = self.friend_set.all()

        friends_list = [
            self._distance_from_friend(friend) for friend in friends
        ]

        self.friends_route = sorted(friends_list, key=itemgetter('distance'))


    def _distance_from_friend(self, friend):
        import math

        dist = math.hypot(friend.x - self.x, friend.y - self.y)
        dist = round(dist, 2)

        return {'id': friend.id, 'distance': dist}


    def world_size(self):
        from random import randint

        return randint(0, 100)


    def __str__(self):
        return '{0} -> x: {1}; y: {2}'.format(
            self.id, self.x, self.y
        )

