# Generated by Django 4.0.7 on 2022-08-14 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='User', max_length=50)),
                ('title', models.CharField(max_length=15)),
                ('desc', models.TextField()),
            ],
        ),
    ]