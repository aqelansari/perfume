# Generated by Django 3.2.16 on 2022-12-27 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_ingredientsinventory_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientsinventory',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
