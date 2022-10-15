# Generated by Django 4.0.5 on 2022-06-24 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Contact phone'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='web',
            field=models.URLField(blank=True, verbose_name='website Address'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='zip_code',
            field=models.CharField(blank=True, max_length=20, verbose_name='Zip Code'),
        ),
    ]