# Generated by Django 5.0.1 on 2024-02-11 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_rename_write_post_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]