# Generated by Django 5.0.14 on 2025-05-03 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
