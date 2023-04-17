from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class User(AbstractUser):
    email = models.EmailField(verbose_name='email',
                              max_length=225, unique=True)
    is_admin = models.BooleanField(default=False)
    REQUIRED_FIELDS = ('username', 'first_name', 'is_admin')
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
    

class Stories(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, null=False)
    tags = models.CharField(max_length=10, null=False, verbose_name='tags')
    story = models.TextField(null=False)

    def __str__(self):
        return self.title
