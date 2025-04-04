# Generated by Django 5.1.7 on 2025-03-26 17:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0002_alter_profile_created_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='auth_user',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.CharField(editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='type',
            field=models.CharField(choices=[('customer', 'customer'), ('business', 'business')], editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.IntegerField(default=1, editable=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(editable=False, max_length=50),
        ),
    ]
