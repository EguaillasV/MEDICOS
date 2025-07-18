# Generated by Django 5.0.7 on 2025-06-29 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_remove_patient_created_at_patient_activo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='estado_civil',
            field=models.CharField(choices=[('S', 'Soltero'), ('C', 'Casado'), ('D', 'Divorciado'), ('V', 'Viudo'), ('U', 'Unido')], max_length=12, verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1, verbose_name='Sexo'),
        ),
    ]
