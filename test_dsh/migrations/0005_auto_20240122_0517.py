# Generated by Django 3.2.13 on 2024-01-22 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_dsh', '0004_auto_20240122_0319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testc',
            name='id',
        ),
        migrations.AlterField(
            model_name='testc',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
