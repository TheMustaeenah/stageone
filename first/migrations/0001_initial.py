# Generated by Django 4.1.1 on 2022-10-29 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slackUsername', models.CharField(max_length=50)),
                ('backend', models.BooleanField()),
                ('age', models.IntegerField()),
                ('bio', models.TextField(max_length=250)),
            ],
        ),
    ]