# Generated by Django 4.2.5 on 2023-10-19 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog_app", "0008_postmodel_comments"),
    ]

    operations = [
        migrations.CreateModel(
            name="CommentPostModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=80)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("active", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "comment",
                "verbose_name_plural": "comments",
                "ordering": ["created_on"],
            },
        ),
        migrations.RemoveField(
            model_name="postmodel",
            name="comments",
        ),
        migrations.AddField(
            model_name="postcategorymodel",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="postmodel",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name="Comment",
        ),
        migrations.AddField(
            model_name="commentpostmodel",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post_comments",
                to="blog_app.postmodel",
            ),
        ),
    ]
