# Generated by Django 5.0.1 on 2024-02-06 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('mines_count', models.IntegerField()),
                ('field', models.JSONField(default=list)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
