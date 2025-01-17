# Generated by Django 5.1.2 on 2024-10-20 15:30

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=1000, null=True)),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'O valor não pode ser inferior a 0'), django.core.validators.MaxValueValidator(5, 'O valor não pode ser superior a 5')])),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.movie')),
            ],
        ),
    ]
