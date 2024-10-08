# Generated by Django 5.1.1 on 2024-10-08 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_module', '0002_books_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='overview',
            field=models.TextField(blank=True, default=None, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(null=True, upload_to='admin_module/books/images/'),
        ),
    ]
