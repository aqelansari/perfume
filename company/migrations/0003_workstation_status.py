# Generated by Django 3.2.16 on 2022-11-03 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='workstation',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
