# Generated by Django 5.0 on 2023-12-05 13:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"verbose_name": "პოსტი", "verbose_name_plural": "პოსტები"},
        ),
    ]