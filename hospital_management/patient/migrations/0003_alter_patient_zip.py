# Generated by Django 3.2 on 2021-06-01 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_alter_patient_contact_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='zip',
            field=models.CharField(max_length=10),
        ),
    ]
