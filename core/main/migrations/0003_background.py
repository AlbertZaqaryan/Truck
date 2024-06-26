# Generated by Django 5.0.6 on 2024-05-08 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='Background picture')),
                ('text1', models.TextField(verbose_name='Text')),
                ('text2', models.TextField(verbose_name='Text')),
                ('button_name', models.CharField(max_length=20, verbose_name='Button name')),
            ],
        ),
    ]
