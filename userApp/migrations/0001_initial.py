# Generated by Django 5.0.6 on 2024-07-05 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
    ]
