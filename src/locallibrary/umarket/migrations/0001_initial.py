# Generated by Django 2.1.2 on 2018-10-31 19:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productID', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('userID', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('name', models.CharField(help_text='Product', max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('seller_rating', models.IntegerField()),
                ('category', models.CharField(default='Some Category', help_text='Category', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Enter email address', max_length=254)),
                ('password', models.CharField(help_text='Enter password', max_length=40)),
                ('name', models.CharField(help_text='Full name', max_length=20)),
                ('rating', models.IntegerField()),
                ('userID', models.UUIDField(default=uuid.uuid4, unique=True)),
            ],
        ),
    ]
