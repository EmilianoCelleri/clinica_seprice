# Generated by Django 4.0.5 on 2024-06-13 01:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historias_medicas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historiaclinica',
            name='tratamiento',
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='diagnostico',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]