# Generated by Django 3.2.16 on 2022-11-02 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ingredient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientsInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('per_unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('added_on', models.DateTimeField()),
                ('updated_on', models.DateTimeField(blank=True, null=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='inventory_added_by', to=settings.AUTH_USER_MODEL)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ingredient.ingredient')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='inventory_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ingredient_inventory',
            },
        ),
    ]
