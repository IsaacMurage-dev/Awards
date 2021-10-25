from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Profile
        fields = ('image', 'bio')

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'post_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        
class ProjectRatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['project', 'pub_date', 'user']

    