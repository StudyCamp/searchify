# Generated by Django 3.2 on 2021-05-02 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchifyApp', '0005_alter_tag_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(default=None, max_length=32),
        ),
    ]
