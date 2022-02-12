from django.test import TestCase
from .models import SharePost, likeusers
from django.contrib.auth import get_user_model


User = get_user_model()


class PostLikeTestCase(TestCase):

    def setUp(self):
        user = User.objects.filter(id=1)
        print('in usere', user)
        print(SharePost.own_like.own_like(user, like=True))

    def test_like_own(self):
        print(SharePost.objects.all())