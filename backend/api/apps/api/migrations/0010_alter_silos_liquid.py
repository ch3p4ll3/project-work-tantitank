# Generated by Django 4.1.3 on 2022-12-02 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_logs_options_liquids_co2max_liquids_co2min_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='silos',
            name='liquid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.liquids'),
        ),
    ]
