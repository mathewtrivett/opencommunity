# Generated by Django 2.2.2 on 2019-06-17 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='eligibility',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service', to='api.Eligibility'),
        ),
    ]