# Generated by Django 4.2.5 on 2023-10-07 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog_app", "0004_alter_postmodel_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postmodel",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/posts",
                verbose_name="image post (770*340px)",
            ),
        ),
        migrations.AlterField(
            model_name="postmodel",
            name="slug",
            field=models.SlugField(
                default="", max_length=200, unique=True, verbose_name="name in url"
            ),
        ),
    ]
