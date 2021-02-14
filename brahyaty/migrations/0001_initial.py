# Generated by Django 3.0.2 on 2020-08-07 09:40

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BadHabbit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('dangers', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('badget_min', models.IntegerField()),
                ('badget_max', models.IntegerField()),
                ('efficacite', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('bad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brahyaty.BadHabbit')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('order', models.IntegerField()),
                ('date_daily', models.IntegerField()),
                ('subs_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brahyaty.Subs')),
            ],
        ),
    ]
