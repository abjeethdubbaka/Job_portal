# Generated by Django 3.2.2 on 2021-05-14 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidates', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidates',
            name='are_they_willing_to_relocate',
        ),
        migrations.AddField(
            model_name='candidates',
            name='city_live_in',
            field=models.CharField(default='hyderabd', max_length=20),
        ),
        migrations.AddField(
            model_name='candidates',
            name='mobile',
            field=models.CharField(default='950', max_length=100),
        ),
        migrations.AddField(
            model_name='candidates',
            name='salary_expectations',
            field=models.IntegerField(default=2000),
        ),
        migrations.AddField(
            model_name='candidates',
            name='willing_to_relocate',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='candidates',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=122),
        ),
        migrations.AlterField(
            model_name='candidates',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
