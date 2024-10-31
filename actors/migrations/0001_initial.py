# Generated by Django 5.1.2 on 2024-10-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, choices=[('BRAZIL', 'BR'), ('UNITED STATES', 'USA')], max_length=100, null=True)),
            ],
        ),
    ]
