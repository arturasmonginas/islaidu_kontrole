# Generated by Django 3.0.8 on 2020-07-26 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrole', '0004_auto_20200726_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='islaidos',
            name='data',
            field=models.DateField(null=True, verbose_name='Data'),
        ),
    ]
