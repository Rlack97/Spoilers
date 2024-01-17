# Generated by Django 4.1.3 on 2022-11-21 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_movie_popularity'),
        ('accounts', '0004_alter_user_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='wish_list',
        ),
        migrations.AddField(
            model_name='user',
            name='wish_list',
            field=models.ManyToManyField(related_name='wish_users', to='movies.movie'),
        ),
    ]