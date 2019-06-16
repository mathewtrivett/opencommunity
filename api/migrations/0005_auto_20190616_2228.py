# Generated by Django 2.2.2 on 2019-06-16 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='organisation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Organisation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='taxonomy',
            field=models.ManyToManyField(related_name='services', to='api.Taxonomy'),
        ),
    ]