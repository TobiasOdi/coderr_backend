# Generated by Django 5.1.7 on 2025-03-30 13:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers_app', '0002_offer_created_at_offer_description_offer_image_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='user',
            field=models.ForeignKey(blank=True, default=15, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='user',
            field=models.ForeignKey(blank=True, default=13, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
