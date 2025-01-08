# Generated by Django 5.1.4 on 2025-01-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karte', '0004_karte_utakmica'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='karte',
            name='cena',
        ),
        migrations.AddField(
            model_name='preostalokarata',
            name='cena',
            field=models.DecimalField(decimal_places=2, default=5000.0, max_digits=6),
        ),
    ]