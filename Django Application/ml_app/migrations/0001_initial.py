# Generated by Django 3.2.5 on 2024-03-29 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.PositiveIntegerField()),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]
