# Generated by Django 4.0.3 on 2022-04-10 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Hospital', '0003_remove_hospital_city_remove_hospital_kebele_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='Account_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
