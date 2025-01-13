# Generated by Django 5.1.4 on 2025-01-07 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('discounted_price', models.IntegerField()),
                ('description', models.TextField()),
                ('rating', models.FloatField()),
                ('image', models.CharField(max_length=300)),
            ],
        ),
    ]
