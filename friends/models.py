from django.db import models


class Friend(models.Model):
    me = models.BooleanField(default=False)
    x = models.IntegerField()
    y = models.IntegerField()

    friends = models.ForeignKey('self', null=True, blank=True)


    def add_friend(self, f):
        if self.friend_set.filter(x=f.x).filter(
            y=f.y
        ).count() > 0:
            return False
        else:
            f.save()
            self.friend_set.add(f)
            return True


    def generate_friends(self):
        from random import randint

        self.friend_set.clear()
        friends_num = randint(1, 10)
        for i in range(friends_num):
            while True:
                x = randint(0, 100)
                y = randint(0, 100)
                f = Friend(x=x, y=y)
                if self.add_friend(f):
                    break


    def __str__(self):
        return '{0} -> x: {1}; y: {2}'.format(
            self.id, self.x, self.y
        )

