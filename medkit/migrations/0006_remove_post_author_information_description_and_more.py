# Generated by Django 4.2 on 2023-04-09 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("medkit", "0005_post_comment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="author",
        ),
        migrations.AddField(
            model_name="information",
            name="description",
            field=models.CharField(default="default description", max_length=30),
        ),
        migrations.DeleteModel(
            name="Comment",
        ),
        migrations.DeleteModel(
            name="Post",
        ),
    ]
