from django.db import models


class Tutor(models.Model):
    tutor_name = models.CharField(verbose_name='Имя Фамилия', max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    tutor_phone = models.CharField(verbose_name='телефон', max_length=13)
    tutor_info = models.TextField(verbose_name='инфо')
    tutor_photo = models.ImageField(upload_to='tutor/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.tutor_name
