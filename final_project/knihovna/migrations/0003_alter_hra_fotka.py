# Generated by Django 5.0.6 on 2024-06-14 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knihovna', '0002_hra_fotka'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hra',
            name='fotka',
            field=models.ImageField(default='uploads/default.png', upload_to='uploads/{% Hra.nazev.value() %}/'),
        ),
    ]
