# Generated by Django 5.1.7 on 2025-04-01 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers_app', '0004_offerdetails_offer_min_price_offer_details_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='details',
        ),
        migrations.AlterField(
            model_name='offer',
            name='image',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='details',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
