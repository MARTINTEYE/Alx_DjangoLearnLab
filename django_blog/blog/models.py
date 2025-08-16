from django.db import models
from django.contrib.auth.models import User

# Your existing Post model (keep it as-is)
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

# New Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
