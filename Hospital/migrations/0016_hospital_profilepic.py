# Generated by Django 4.0.3 on 2022-04-20 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0015_alter_bloodrequest_blood_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='ProfilePic',
            field=models.FileField(blank=True, default='profilepic/defaultprofile.jpeg.', null=True, upload_to='profilepic/'),
        ),
    ]