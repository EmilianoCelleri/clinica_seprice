# Generated by Django 4.0.5 on 2024-06-02 19:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registro', '0003_medico_especialidad_alter_especialidad_especialidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('duracion', models.DurationField(default=datetime.timedelta(seconds=900))),
                ('estado', models.CharField(choices=[('D', 'Disponible'), ('R', 'Reservado'), ('C', 'Cancelado')], default='D', max_length=1)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.especialidad')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.medico')),
            ],
            options={
                'unique_together': {('medico', 'fecha', 'hora_inicio')},
            },
        ),
    ]
