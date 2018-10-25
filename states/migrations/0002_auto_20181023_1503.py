# Generated by Django 2.1.2 on 2018-10-23 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
        ('states', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='countryId',
        ),
        migrations.AddField(
            model_name='state',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Country', to='countries.Country'),
        ),
    ]