# Generated by Django 5.1.2 on 2024-10-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0002_alter_actor_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='nationality',
            field=models.CharField(blank=True, choices=[('BRAZIL', 'BR'), ('USA', 'UNITED STATES')], max_length=100, null=True),
        ),
    ]
