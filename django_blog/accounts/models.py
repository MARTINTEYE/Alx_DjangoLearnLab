from django.conf import settings
from django.db import models
from django.core.validators import FileExtensionValidator

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextAreaField = models.TextField(blank=True)
    avatar = models.ImageField(
        upload_to="avatars/",
        blank=True,
        validators=[FileExtensionValidator(["png", "jpg", "jpeg", "webp"])]
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"
