from django.conf import settings
from django.db import models
from django.urls import reverse


class Tutor(models.Model):
    tutor_name = models.CharField(verbose_name='Имя Фамилия', max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    tutor_phone = models.CharField(verbose_name='телефон', max_length=13)
    tutor_info = models.TextField(verbose_name='инфо')
    tutor_photo = models.ImageField(upload_to='tutor/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.tutor_name

    def get_absolute_url(self):
        return reverse('reception:create_reception',
                       args=[self.slug])

    def get_create_feedback_url(self):
        return reverse('reception:create_feedback', args=[self.slug])

    def get_see_feedback_url(self):
        return reverse('reception:see_feedback', args=[self.slug])


class Reception(models.Model):
    reception_date_time = models.DateTimeField(verbose_name='дата приема')
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    user = models.CharField(max_length=50, blank=True)


class Feedback(models.Model):
    feedback_text = models.TextField(verbose_name='написать отзыв')
    created = models.DateTimeField(auto_now_add=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(verbose_name='телефон', max_length=13, blank=True, null=True)

    def __str__(self):
        return str(self.user) + ' profile'
