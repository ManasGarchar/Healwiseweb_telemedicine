# Generated by Django 5.0.3 on 2024-04-03 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_remove_payment_user_id_alter_appointment_user_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='disease_nm',
            field=models.CharField(blank=True, max_length=59),
        ),
    ]