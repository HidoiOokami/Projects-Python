# Generated by Django 2.2.3 on 2019-07-20 02:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190719_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
