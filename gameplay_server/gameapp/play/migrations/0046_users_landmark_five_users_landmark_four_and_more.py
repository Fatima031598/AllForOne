# Generated by Django 4.0.3 on 2022-03-24 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0045_alter_landmarks_total_challenge_completions'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='landmark_five',
            field=models.ForeignKey(default='03ee9967-9056-4cc1-9954-ff10f9d19973', on_delete=django.db.models.deletion.CASCADE, related_name='challenge_five', to='play.landmarks'),
        ),
        migrations.AddField(
            model_name='users',
            name='landmark_four',
            field=models.ForeignKey(default='03ee9967-9056-4cc1-9954-ff10f9d19973', on_delete=django.db.models.deletion.CASCADE, related_name='challenge_four', to='play.landmarks'),
        ),
        migrations.AddField(
            model_name='users',
            name='landmark_one',
            field=models.ForeignKey(default='03ee9967-9056-4cc1-9954-ff10f9d19973', on_delete=django.db.models.deletion.CASCADE, related_name='challenge_one', to='play.landmarks'),
        ),
        migrations.AddField(
            model_name='users',
            name='landmark_seven',
            field=models.ForeignKey(default='03ee9967-9056-4cc1-9954-ff10f9d19973', on_delete=django.db.models.deletion.CASCADE, related_name='challenge_seven', to='play.landmarks'),
        ),
        migrations.AddField(
            model_name='users',
            name='landmark_six',
            field=models.ForeignKey(default='03ee9967-9056-4cc1-9954-ff10f9d19973', on_delete=django.db.models.deletion.CASCADE, related_name='challenge_six', to='play.landmarks'),
        ),
        migrations.AddField(
            model_name='users',
            name='landmark_three',
            field=models.ForeignKey(default='03ee9967-9056-4cc1-9954-ff10f9d19973', on_delete=django.db.models.deletion.CASCADE, related_name='challenge_three', to='play.landmarks'),
        ),
        migrations.AddField(
            model_name='users',
            name='landmark_two',
            field=models.ForeignKey(default='03ee9967-9056-4cc1-9954-ff10f9d19973', on_delete=django.db.models.deletion.CASCADE, related_name='challenge_two', to='play.landmarks'),
        ),
    ]
