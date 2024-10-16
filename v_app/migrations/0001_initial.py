# Generated by Django 5.0.4 on 2024-04-17 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=50)),
                ('cat_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='contact')),
            ],
        ),
        migrations.CreateModel(
            name='Medicines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_name', models.CharField(max_length=150)),
                ('med_use', models.CharField(max_length=150)),
                ('med_price', models.CharField(max_length=20)),
                ('med_image', models.ImageField(upload_to='medicines')),
                ('med_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='PharmLab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=100)),
                ('test_des', models.CharField(max_length=200)),
                ('test_price', models.CharField(max_length=20)),
                ('test_image', models.ImageField(upload_to='pharmlab')),
                ('test_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=50)),
                ('pro_use', models.CharField(max_length=50)),
                ('pro_price', models.CharField(max_length=20)),
                ('pro_image', models.ImageField(upload_to='product')),
                ('pro_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(max_length=50)),
                ('cus_phone', models.CharField(blank=True, max_length=12, null=True)),
                ('cus_email', models.EmailField(max_length=254)),
                ('order_date', models.DateField()),
                ('order_on', models.DateField(auto_now=True)),
                ('cat_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v_app.category')),
                ('pro_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v_app.product')),
            ],
        ),
    ]
