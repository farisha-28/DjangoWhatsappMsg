# Generated by Django 5.0.6 on 2024-05-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_remove_messagehandler_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagehandler',
            name='email',
            field=models.TextField(default='Default email'),
        ),
        migrations.AddField(
            model_name='messagehandler',
            name='message',
            field=models.TextField(default='Default message'),
        ),
    ]
