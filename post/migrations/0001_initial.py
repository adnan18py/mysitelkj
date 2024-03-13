# Generated by Django 5.0.1 on 2024-03-11 15:47

import django.db.models.deletion
import taggit.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('text', models.TextField(null=True, verbose_name='متن')),
                ('writer', models.CharField(max_length=30, verbose_name='نویسنده')),
                ('img', models.ImageField(null=True, upload_to='images', verbose_name='عکس')),
                ('alt', models.CharField(max_length=100, null=True, verbose_name='موضوع تصویر')),
                ('crated_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(allow_unicode=True, null=True, unique=True, verbose_name='آدرس  پست')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='نام کاربری')),
                ('text', models.TextField(verbose_name='متن کامنت')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
            ],
        ),
    ]
