# Generated by Django 2.2 on 2019-05-26 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodega', '0002_auto_20190428_0556 00-13-37-948'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('oc_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('sku', models.IntegerField()),
                ('client', models.CharField(max_length=255)),
                ('provider', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('price', models.IntegerField()),
                ('state', models.CharField(default='creada', max_length=255)),
                ('channel', models.CharField(max_length=255)),
                ('deadline', models.DateTimeField()),
                ('finished', models.BooleanField(default=True)),
            ],
        ),
    ]
