# Generated by Django 4.2.9 on 2024-01-12 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialnex', '0004_like_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers_count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]
