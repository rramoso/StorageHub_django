# Generated by Django 2.2.1 on 2019-05-29 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]