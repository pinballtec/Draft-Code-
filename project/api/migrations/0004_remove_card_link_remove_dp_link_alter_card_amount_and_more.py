# Generated by Django 4.0.4 on 2022-05-23 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_paybylink_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='link',
        ),
        migrations.RemoveField(
            model_name='dp',
            name='link',
        ),
        migrations.AlterField(
            model_name='card',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='card',
            name='created_at',
            field=models.TimeField(auto_now_add=True, unique=True),
        ),
        migrations.AlterField(
            model_name='dp',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='paybylink',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
