# Generated by Django 4.0.3 on 2022-04-19 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0027_alter_donationrequestformresult_donor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='Bloodgroup',
            field=models.CharField(blank=True, choices=[(None, 'Select type'), ('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='ProfilePic',
            field=models.FileField(blank=True, default='profilepic/defaultprofile.jpeg.', null=True, upload_to='profilepic/'),
        ),
    ]