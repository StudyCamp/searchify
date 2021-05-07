# Generated by Django 3.2 on 2021-04-30 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchifyApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(default=None, max_length=32)),
                ('tag_post', models.ManyToManyField(related_name='tagged_posts', to='searchifyApp.Post')),
            ],
        ),
    ]