from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.db.models import Q
from account.models import UserProfile

User = get_user_model()


class UserOwnlikeManager(models.Manager):

    def own_like(self, user, like = None): # mitoni badan bejash khode parametr o bzri beja args
        if like:
            return self.filter(user = user).update(like = True)
        
        



class SharePost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_sharepost')
    img = models.ImageField(upload_to = 'post_media/', null=True, blank = True)
    video = models.FileField(upload_to = 'post_media/', null= True, blank = True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    save_post = models.BooleanField(default=False, blank=True)
    like = models.BooleanField(default=False, blank=True)
    like_number = models.IntegerField(default=0)
    objects = models.Manager()
    own_like = UserOwnlikeManager()

    def clean(self, *args, **kwargs):
        if self.img == None and self.video == None:
            raise ValidationError('you have to post smth')

        elif self.img != None and self.video != None:
            raise ValidationError('you cant post img and video at same time')
        
        if self.like == True:
            self.like_number += 1

        return super().clean(*args, **kwargs)

    # class Meta:
    #     constraints = [
    #         models.CheckConstraint(
    #             check=models.Q(video_isnull = False) |
    #             models.Q(img_isnull = False),
    #             name = 'one of the two not null'
    #         )
    #     ]


class LikePostManager(models.Manager):

    def liking(self, post, like = None): # like bayad true shavad post ha mgire
        liking = self.get(post = post)

        if self.filter(like=True):
            liking += 1
            return self.save()
        


class likeusers(models.Model):
    post = models.ForeignKey(SharePost, on_delete=models.CASCADE, related_name='like_post')
    user = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, related_name='like_users')
    save_post = models.BooleanField(default=False, blank=True)
    like = models.BooleanField(default=False, blank=True)
    objects = models.Manager()
    liking = LikePostManager()


class SaveCollection(models.Model):
    save_title = models.CharField(max_length=255)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_savepost')
    files = models.JSONField(null = True, blank = True)

