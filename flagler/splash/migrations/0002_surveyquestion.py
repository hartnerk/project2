# Generated by Django 4.2.13 on 2024-07-27 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splash', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('answer', models.CharField(max_length=50)),
            ],
        ),
    ]
