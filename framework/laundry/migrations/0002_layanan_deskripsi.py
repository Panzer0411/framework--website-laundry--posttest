# Generated by Django 5.1.1 on 2024-10-01 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='layanan',
            name='deskripsi',
            field=models.TextField(default='DESKRIPSI BELUM DIISI'),
            preserve_default=False,
        ),
    ]
