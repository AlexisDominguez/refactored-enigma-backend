# Generated by Django 2.1 on 2022-10-16 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notebooks', '0001_initial'),
        ('notes', '0003_auto_20221013_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='notebook',
            field=models.ForeignKey(
                default=2, on_delete=django.db.models.deletion.CASCADE, to='notebooks.Notebooks'),
            preserve_default=False,
        ),
    ]
