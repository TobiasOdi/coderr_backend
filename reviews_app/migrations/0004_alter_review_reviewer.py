# Generated by Django 5.1.7 on 2025-03-29 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_app', '0003_alter_review_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='reviewer',
            field=models.IntegerField(blank=True),
        ),
    ]
