# Generated by Django 5.0.1 on 2024-03-11 17:24

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
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='نام محصول')),
                ('cap', models.TextField(null=True, verbose_name='کپشن')),
                ('text', models.TextField(null=True, verbose_name='توضیحات')),
                ('img', models.ImageField(null=True, upload_to='', verbose_name='عکس محصول')),
                ('price', models.PositiveIntegerField(null=True, verbose_name='(تومان)قیمت محصول')),
                ('alt', models.CharField(max_length=100, null=True, verbose_name='موضوع تصویر')),
                ('slug', models.SlugField(allow_unicode=True, null=True, unique=True, verbose_name='آدرس  پست')),
                ('off', models.BooleanField(default=False)),
                ('related_products', models.ManyToManyField(blank=True, to='products.products')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='نام کاربری')),
                ('text', models.TextField(verbose_name='متن کامنت')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
    ]
