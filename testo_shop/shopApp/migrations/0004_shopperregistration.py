# Generated by Django 3.2.3 on 2021-06-30 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0003_alter_shopperproduct_pro_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopperRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('shop_name', models.CharField(max_length=100)),
                ('user_mail', models.CharField(max_length=50)),
                ('user_mobile', models.CharField(max_length=12, unique=True)),
                ('user_address', models.TextField(max_length=200)),
                ('user_B_date', models.DateField()),
                ('user_MBank', models.CharField(max_length=50)),
            ],
        ),
    ]
