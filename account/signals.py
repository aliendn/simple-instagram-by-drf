# from .models import FriendUser
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save


# def create_circle(sender, **kw):
#     user = kw["instance"]
#     if kw["created"]:
#         c = FriendUser(user=user)
#         c.save()

# post_save.connect(create_circle, sender=User)