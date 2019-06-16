# Generated by Django 2.2.2 on 2019-06-16 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20190616_2247'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taxonomy',
            options={'verbose_name_plural': 'Taxonomy'},
        ),
        migrations.AddField(
            model_name='organisation',
            name='physical_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.PhysicalAddress'),
        ),
    ]
