# Generated by Django 4.0.3 on 2022-04-11 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0012_remove_bloodrequest_hospital_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodrequest',
            name='Hospital_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hospital.hospital'),
        ),
    ]
