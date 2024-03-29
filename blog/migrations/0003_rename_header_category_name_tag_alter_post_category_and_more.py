# Generated by Django 4.0.4 on 2022-05-09 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_header'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='header',
            new_name='name_tag',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='home', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
