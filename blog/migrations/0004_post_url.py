# Generated by Django 4.0.4 on 2022-05-10 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_header_category_name_tag_alter_post_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
