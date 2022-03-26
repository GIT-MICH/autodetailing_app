# Generated by Django 3.0.6 on 2022-03-25 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autodetailing_app', '0008_service_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='created',
            new_name='termin_realizacji',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='service',
        ),
        migrations.AddField(
            model_name='cart',
            name='services',
            field=models.ManyToManyField(to='autodetailing_app.Service'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Dodaj plik'),
        ),
    ]
