# Generated by Django 3.0.8 on 2020-07-26 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kontrole', '0008_auto_20200726_1920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='islaidos',
            options={'ordering': ['-data'], 'verbose_name': 'Išlaida', 'verbose_name_plural': 'Išlaidos'},
        ),
    ]