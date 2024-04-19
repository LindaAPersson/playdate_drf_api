# Generated by Django 5.0.4 on 2024-04-19 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playdate', '0002_playdate_suitable_age_playdate_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playdate',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='playdate',
            name='suitable_age',
            field=models.CharField(choices=[('all', 'All Ages'), ('infant', 'Infant (0-2 years)'), ('toddler', 'Toddler (2-5 years)'), ('child', 'Child (5-12 years)'), ('teenager', 'Teenager (13-18 years)')], max_length=20),
        ),
    ]
