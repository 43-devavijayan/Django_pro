# Generated by Django 3.0.8 on 2020-07-09 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('age', models.IntegerField()),
                ('email_id', models.EmailField(max_length=254)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]