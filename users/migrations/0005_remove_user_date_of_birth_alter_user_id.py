# Generated by Django 4.1.4 on 2022-12-20 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_groups_remove_user_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
