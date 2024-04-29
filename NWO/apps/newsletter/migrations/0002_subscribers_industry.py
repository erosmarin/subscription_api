# Generated by Django 4.2.11 on 2024-04-26 03:43

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribers',
            name='industry',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Consumer_Health'), (2, 'Beauty'), (3, 'Tech')], max_length=3, null=True),
        ),
    ]
