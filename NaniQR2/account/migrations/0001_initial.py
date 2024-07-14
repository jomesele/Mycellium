# Generated by Django 5.0.6 on 2024-07-05 14:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('type', models.CharField(choices=[('AGENT', 'agent'), ('STORE', 'store'), ('ADMINA', 'admina')], default='AGENT', max_length=8)),
                ('phone', models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('name', models.CharField(max_length=100)),
                ('qrImg', models.ImageField(upload_to='media/user_qr')),
                ('address', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('storeQrImg', models.ImageField(upload_to='media/store_qr')),
                ('logo', models.ImageField(upload_to='media/store_logo')),
                ('category1', models.CharField(choices=[('Electronics', 'electronics'), ('Fashion', 'fashion'), ('Books', 'books'), ('', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], default='AGENT', max_length=100)),
                ('prod', models.CharField(choices=[('Electronics', 'electronics'), ('Fashion', 'fashion'), ('Books', 'books'), ('', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], default='AGENT', max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_agent', models.BooleanField(default=False)),
                ('is_store', models.BooleanField(default=False)),
                ('is_admina', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Admina',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('account.myuser',),
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('account.myuser',),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('account.myuser',),
        ),
    ]