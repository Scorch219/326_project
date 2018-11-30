# Generated by Django 2.1.2 on 2018-11-29 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('umarket', '0010_auto_20181129_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='favorited',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='umarket.Profile'),
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_requests_created', to='umarket.Profile'),
        ),
    ]