# Generated by Django 3.2.16 on 2022-12-16 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0003_remove_container_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='volume',
            field=models.IntegerField(),
        ),
    ]
