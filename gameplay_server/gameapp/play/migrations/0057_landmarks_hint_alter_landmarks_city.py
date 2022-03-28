# Generated by Django 4.0.3 on 2022-03-28 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0056_timerecords_completion_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='landmarks',
            name='hint',
            field=models.CharField(default='', editable=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='landmarks',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='play.cities'),
        ),
    ]
