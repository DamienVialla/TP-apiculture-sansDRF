# Generated by Django 5.0.1 on 2024-01-08 09:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_ruche_name_alter_ruche_contamination_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheptel',
            name='owner',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='hive',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interventions', to='principal.ruche'),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='type_action',
            field=models.CharField(choices=[('Suppression_cellules_royales', 'Suppression_cellules_royales'), ('verification_santé', 'Vérification santé'), ('Récole', 'Récolte'), ('Pose_hausses', 'Pose hausses'), ('Destruction', 'Destruction'), ('Traitement', 'Traitement')], max_length=100),
        ),
        migrations.AlterField(
            model_name='ruche',
            name='cheptel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.cheptel'),
        ),
        migrations.AlterField(
            model_name='ruche',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='ruche',
            name='owner',
            field=models.CharField(max_length=40),
        ),
    ]
