# Generated by Django 3.2.9 on 2021-11-20 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0002_auto_20211120_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reception_date_time', models.DateTimeField(verbose_name='дата приема')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reception.tutor')),
            ],
        ),
    ]
