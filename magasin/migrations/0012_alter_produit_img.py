# Generated by Django 4.1.2 on 2023-05-17 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0011_alter_produit_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='img',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
    ]