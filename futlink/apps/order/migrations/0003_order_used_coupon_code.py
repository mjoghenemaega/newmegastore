# Generated by Django 3.1.7 on 2021-02-23 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='used_coupon_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]