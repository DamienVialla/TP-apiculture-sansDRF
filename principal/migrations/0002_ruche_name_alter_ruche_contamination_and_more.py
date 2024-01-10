# Generated by Django 5.0.1 on 2024-01-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruche',
            name='name',
            field=models.CharField(default='toto', max_length=40),
        ),
        migrations.AlterField(
            model_name='ruche',
            name='contamination',
            field=models.CharField(choices=[('acarapisose', 'acarapisose'), ('loque_américaine', 'loque américaine'), ('infestation_par_le petit_coléoptère_des_ruches', 'infestation par_le_petit_coléoptère_des_ruches'), ('infestation_par_l’acarien_Tropilaelaps', 'infestation par l’acarien Tropilaelaps'), ('varroose', 'varroose'), ('aucune', 'Aucune')]),
        ),
        migrations.AlterField(
            model_name='ruche',
            name='queen_birthday',
            field=models.DateField(),
        ),
    ]
