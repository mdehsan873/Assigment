# Generated by Django 4.1.1 on 2022-09-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_alter_company_inception_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='uuid',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
