# Generated by Django 5.0.6 on 2024-07-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('catagories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='product',
            field=models.ManyToManyField(default=1, to='catagories.product'),
        ),
    ]
