# Generated by Django 3.2.3 on 2021-06-30 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0004_shopperregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopperregistration',
            name='user_mail',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
