# Generated by Django 4.1.3 on 2022-11-10 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="image",
            field=models.CharField(
                max_length=255, null=True, unique=True, verbose_name="Image"
            ),
        ),
    ]
