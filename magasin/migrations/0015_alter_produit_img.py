# Generated by Django 4.1.2 on 2023-05-17 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0014_alter_produit_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='img',
            field=models.ImageField(blank=b'I01\n', upload_to=''),
        ),
    ]