# Generated by Django 4.2.13 on 2024-06-15 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knihovna', '0013_uzivatel_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uzivatel',
            name='bio',
            field=models.CharField(blank=True, default='', help_text='Napište něco o sobě', max_length=300, null=True, verbose_name='Bio'),
        ),
    ]
