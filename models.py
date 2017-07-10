from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    # add your fields here

    def __str__(self):
        return 'User Profile for %(username)s' % dict(username=self.username)


# for the fields to appear in django administration site you need to
# go to admin.py file and add the fields you just added above
