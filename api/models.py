from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email',
                              max_length=225, unique=True)
    is_admin = models.BooleanField(default=False)
    REQUIRED_FIELDS = ('username',)
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
    
def upload_to(instance, filename):
    # return 'images/{filename}'.format(filename=filename)
    return f'images/{filename}'

class Stories(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, null=False)
    tags = models.CharField(max_length=10, null=False, verbose_name='tags')
    created_at = models.DateField(auto_now_add=True, null=True)
    story = models.TextField(null=False)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.title
    

    

