# Generated by Django 3.0.3 on 2020-02-27 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alpaca_app', '0009_auto_20200227_1416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient_variant',
            old_name='disease_id',
            new_name='variant_id',
        ),
        migrations.AlterField(
            model_name='patient_cancer',
            name='cancer_diagnosis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='alpaca_app.Cancer_diagnosis'),
        ),
        migrations.AlterField(
            model_name='patient_cancer',
            name='patient_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='alpaca_app.Patient'),
        ),
        migrations.AlterField(
            model_name='patient_disease',
            name='disease_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='alpaca_app.Disease'),
        ),
        migrations.AlterField(
            model_name='patient_disease',
            name='patient_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='alpaca_app.Patient'),
        ),
        migrations.AlterField(
            model_name='patient_variant',
            name='patient_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='alpaca_app.Patient'),
        ),
        migrations.AlterField(
            model_name='patient_variant',
            name='variant_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='alpaca_app.Variant'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='criteria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='alpaca_app.Classification'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='gene_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='alpaca_app.Gene'),
        ),
        migrations.AlterField(
            model_name='variant_sequencer',
            name='sequencer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='alpaca_app.Sequencer'),
        ),
        migrations.AlterField(
            model_name='variant_sequencer',
            name='variant_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='alpaca_app.Variant'),
        ),
    ]
