# Generated by Django 5.1.4 on 2024-12-24 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210805_1926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='News',
            new_name='news',
        ),
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(upload_to='imgs/'),
        ),
    ]
