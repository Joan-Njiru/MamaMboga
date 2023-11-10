# Generated by Django 4.2.1 on 2023-06-19 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(max_length=32)),
                ('last_Name', models.CharField(max_length=32)),
                ('phone_Number', models.PositiveIntegerField()),
                ('email', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=32)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
