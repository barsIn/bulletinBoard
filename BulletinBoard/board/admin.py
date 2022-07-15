from django import forms
from django.contrib import admin
from .models import Advertisement, Response
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AdvertisementAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Advertisement
        fields = '__all__'


class AdvertisementAdmin(admin.ModelAdmin):
    form = AdvertisementAdminForm


admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(Response)
# Register your models here.
