from django.forms import ModelForm, BooleanField
from .models import Advertisement, Response


class AdvCreateForm(ModelForm):
    # check_box = BooleanField(label='Подтвердить создание')


    class Meta:
        model = Advertisement
        fields = ['heading', 'text', 'category', 'category']

class RespCreateForm(ModelForm):
    # check_box = BooleanField(label='Подтвердить создание')


    class Meta:
        model = Response
        fields = ['tekst',]