# Generated by Django 4.1.7 on 2023-04-12 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='a', max_length=255),
        ),
    ]