# Generated by Django 3.2.16 on 2022-12-13 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0009_auto_20221213_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientnotes',
            name='notes',
            field=models.CharField(max_length=50),
        ),
    ]