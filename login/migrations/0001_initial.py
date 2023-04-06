# Generated by Django 4.1 on 2023-04-06 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=64)),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
