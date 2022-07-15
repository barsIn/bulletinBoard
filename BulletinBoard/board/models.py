from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Advertisement(models.Model):
    CATEGORY_CHOICES = [
        ('TK', 'Tanks'),
        ('HE', 'Heals'),
        ('DD', 'DD'),
        ('MH', 'Merchants'),
        ('GM', 'Guild Masters'),
        ('QG', 'Quest Givers'),
        ('BS', 'Blacksmiths'),
        ('TN', 'Tanners'),
        ('PM', 'Potion Makers'),
        ('SM', 'Spell Masters'),
    ]

    heading = models.CharField(max_length=64)
    text = RichTextUploadingField
    publication_date = models.DateTimeField(auto_now_add=True)
    changepublication_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=2,
                                choices=CATEGORY_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Author')
    rating = models.IntegerField(default=0)
    # responses = models.ForeignKey('Response', on_delete=models.CASCADE, related_name='Отклики')

    class Meta():
        ordering = ['publication_date', '-changepublication_date']
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return f'Объявление {self.heading}, категория {self.category} от {self.author.username}'

    def get_absolute_url(self):
        return f'/adv/{self.id}'

class Response(models.Model):
    tekst = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responseUser')
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='advertisement')
    publication_date = models.DateTimeField(auto_now_add=True)
    changepublication_date = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ['publication_date', '-changepublication_date']
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'

    def __str__(self):
        return f'Отклик от {self.user.username} к объявлению {self.advertisement.heading}: {self.tekst}'

    def get_absolute_url(self):
        return f'/adv/resp/{self.id}'





# Create your models here.
