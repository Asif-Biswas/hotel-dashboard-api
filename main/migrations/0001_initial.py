# Generated by Django 4.2.4 on 2023-08-21 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='spot')),
                ('l_name', models.CharField(max_length=50, verbose_name='Location Name')),
                ('l_tagline', models.CharField(max_length=150, verbose_name='Location Tagline')),
                ('l_summery', models.TextField(max_length=300, verbose_name='Location Summary')),
                ('l_description', models.TextField(max_length=200, verbose_name='Location Description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_tagline', models.CharField(max_length=100, verbose_name='Season Tagline')),
                ('s_name', models.CharField(max_length=50, verbose_name='Season Name')),
                ('s_description', models.TextField(max_length=250, verbose_name='Season Description')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.location')),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sf_title', models.CharField(max_length=50, verbose_name='Title')),
                ('sf_description', models.TextField(max_length=150, verbose_name='Description')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.season')),
            ],
        ),
    ]
