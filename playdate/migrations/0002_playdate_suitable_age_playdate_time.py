# Generated by Django 5.0.4 on 2024-04-16 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playdate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playdate',
            name='suitable_age',
            field=models.CharField(choices=[('infant', 'Infant (0-2 years)'), ('toddler', 'Toddler (2-5 years)'), ('child', 'Child (5-12 years)'), ('teenager', 'Teenager (13-18 years)')], default='toddler', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playdate',
            name='time',
            field=models.TimeField(default='10:00'),
            preserve_default=False,
        ),
    ]
