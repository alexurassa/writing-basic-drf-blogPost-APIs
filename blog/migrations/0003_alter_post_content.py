# Generated by Django 4.1 on 2022-08-22 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_rename_comment_postcomment_rename_tag_posttag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(default="Some content here", max_length=1000),
        ),
    ]
