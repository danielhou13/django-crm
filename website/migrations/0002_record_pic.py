# Generated by Django 4.2.5 on 2023-12-11 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='pic',
            field=models.ImageField(default='default.jpg', upload_to='record_pics'),
        ),
    ]
