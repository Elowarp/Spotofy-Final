from django.forms import ModelForm
from musique.models import Songs

class SongsForm(ModelForm):
    class Meta:
        model = Songs
        fields = ['name', 'author', 'album', 'cover', 'music']