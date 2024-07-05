# Generated by Django 5.0.6 on 2024-07-04 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('adminId', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=500)),
                ('photoFileName', models.ImageField(blank=True, null=True, upload_to='admin_photos/')),
            ],
        ),
    ]