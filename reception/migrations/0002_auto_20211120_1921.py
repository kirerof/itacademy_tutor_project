# Generated by Django 3.2.9 on 2021-11-20 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='tutor_photo',
            field=models.ImageField(blank=True, upload_to='tutor/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='tutor_phone',
            field=models.CharField(max_length=13, verbose_name='телефон'),
        ),
    ]
