# Generated by Django 5.2 on 2025-05-12 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img_url',
            field=models.URLField(default=123),
            preserve_default=False,
        ),
    ]
