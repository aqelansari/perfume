# Generated by Django 3.2.16 on 2022-11-15 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer_order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_added_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='added_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
