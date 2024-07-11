# Generated by Django 3.2.16 on 2022-11-02 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_volume', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_status', models.CharField(choices=[('p', 'Pending'), ('c', 'Completed'), ('ip', 'In Process'), ('e', 'Error'), ('ii', 'Insufficient Ingredients'), ('c', 'Created')], default='c', max_length=2)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('added_on', models.DateTimeField()),
                ('updated_on', models.DateTimeField(blank=True, null=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_added_by', to=settings.AUTH_USER_MODEL)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('production_place', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.workstation')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recipe.recipe')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'customer_order',
            },
        ),
        migrations.CreateModel(
            name='OrderSteps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_info', models.JSONField()),
                ('step_number', models.PositiveIntegerField()),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('step_status', models.CharField(choices=[('p', 'Pending'), ('ip', 'In Process'), ('c', 'Completed'), ('e', 'Error')], default='p', max_length=2)),
                ('customer_order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customer_order.customerorder')),
            ],
            options={
                'db_table': 'order_steps',
            },
        ),
    ]