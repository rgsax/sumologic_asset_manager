# Generated by Django 4.1.1 on 2022-09-20 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SumoInstance',
            fields=[
                ('tag', models.TextField(primary_key=True, serialize=False)),
                ('key', models.TextField()),
                ('url', models.TextField()),
            ],
        ),
    ]
