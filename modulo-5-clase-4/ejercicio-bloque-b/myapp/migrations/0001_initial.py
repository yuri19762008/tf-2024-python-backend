# Generated by Django 5.1.3 on 2025-01-16 08:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Curso",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codigo_curso", models.CharField(max_length=20, unique=True)),
                ("cantidad_estudiantes", models.IntegerField()),
                ("fecha_inicio", models.DateField()),
                ("fecha_termino", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Estudiante",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rut_estudiante", models.CharField(max_length=10, unique=True)),
                ("nombre_estudiante", models.CharField(max_length=100)),
                ("fecha_nacimiento", models.DateField()),
                ("direccion", models.CharField(blank=True, max_length=255, null=True)),
                ("correo", models.EmailField(blank=True, max_length=254, null=True)),
                ("telefono", models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Programa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_programa", models.CharField(max_length=100)),
                ("cantidad_horas", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Relator",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rut_relator", models.CharField(max_length=10, unique=True)),
                ("nombre_relator", models.CharField(max_length=100)),
                (
                    "titulo_relator",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("anios_experiencia", models.IntegerField(blank=True, null=True)),
                ("valor_hora", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="EstudianteCurso",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "curso",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.curso"
                    ),
                ),
                (
                    "estudiante",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.estudiante",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="estudiante",
            name="cursos",
            field=models.ManyToManyField(
                through="myapp.EstudianteCurso", to="myapp.curso"
            ),
        ),
        migrations.CreateModel(
            name="Modulo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_modulo", models.CharField(max_length=100)),
                ("cantidad_horas", models.IntegerField()),
                (
                    "programa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="myapp.programa"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="curso",
            name="programa",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="myapp.programa"
            ),
        ),
        migrations.CreateModel(
            name="RelatorModulo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "modulo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.modulo"
                    ),
                ),
                (
                    "relator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.relator"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="relator",
            name="modulos",
            field=models.ManyToManyField(
                through="myapp.RelatorModulo", to="myapp.modulo"
            ),
        ),
        migrations.AddField(
            model_name="modulo",
            name="relatores",
            field=models.ManyToManyField(
                through="myapp.RelatorModulo", to="myapp.relator"
            ),
        ),
    ]
