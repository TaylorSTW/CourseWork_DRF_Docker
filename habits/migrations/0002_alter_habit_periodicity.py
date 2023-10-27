# Generated by Django 4.2.4 on 2023-08-21 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=models.CharField(choices=[('1', 'каждый день'), ('2', 'каждые два дня'), ('3', 'каждые три дня'), ('4', 'каждые четыре дня'), ('5', 'каждые пять дней'), ('6', 'каждые шесть дней'), ('7', 'каждые семь дней')], max_length=50),
        ),
    ]