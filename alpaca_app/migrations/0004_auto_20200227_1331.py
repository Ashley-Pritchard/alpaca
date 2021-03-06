# Generated by Django 3.0.3 on 2020-02-27 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alpaca_app', '0003_auto_20200227_1306'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='patient_disese',
            new_name='Patient_disease',
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
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='alpaca_app.Patient_cancer'),
        ),
        migrations.AlterField(
            model_name='patient_disease',
            name='patient_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='alpaca_app.Patient'),
        ),
        migrations.AlterField(
            model_name='patient_variant',
            name='disease_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='alpaca_app.Variant'),
        ),
        migrations.AlterField(
            model_name='patient_variant',
            name='patient_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='alpaca_app.Patient'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='classification',
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
