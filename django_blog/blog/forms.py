# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment, Tag
from taggit.forms import TagWidget


# ------------------------
# User Forms
# ------------------------
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "photo"]


# ------------------------
# Post Form with Tags
# ------------------------
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
        widgets = {
            "tags": TagWidget(attrs={"placeholder": "Add tags separated by commas"})
        }


    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()
            # Process tags
            tag_names = self.cleaned_data.get("tags", "")
            if tag_names:
                tag_list = [name.strip() for name in tag_names.split(",") if name.strip()]
                post.tags.clear()
                for tag_name in tag_list:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    post.tags.add(tag)
        return post


# ------------------------
# Comment Form
# ------------------------
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Add a comment..."}),
        max_length=1000,
        label=""
    )

    class Meta:
        model = Comment
        fields = ["content"]
