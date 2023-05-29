# Generated by Django 3.2.9 on 2023-05-05 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Tittle')),
                ('intitution', models.CharField(max_length=150, verbose_name='Tittle')),
                ('datestar', models.DateTimeField(verbose_name='Date Start')),
                ('datefinish', models.DateTimeField(verbose_name='Date Finish')),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Educations',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='LanguagesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Languaje')),
                ('level', models.CharField(choices=[('BASIC', 'BASIC'), ('INTERMEDIATE', 'INTERMEDIATE'), ('ADVANCE', 'ADVANCE')], default='BASIC', max_length=12)),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CVModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('birthdate', models.DateTimeField(verbose_name='Birthdate')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PrincipalApp.educationmodel')),
                ('languaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PrincipalApp.languagesmodel')),
            ],
            options={
                'verbose_name': 'CV',
                'verbose_name_plural': 'CV',
                'ordering': ['id'],
            },
        ),
    ]
