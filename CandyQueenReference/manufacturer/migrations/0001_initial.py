# Generated by Django 3.0.5 on 2020-05-03 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.CharField(blank=True, max_length=999)),
                ('year_of_start', models.DateTimeField()),
            ],
        ),
    ]