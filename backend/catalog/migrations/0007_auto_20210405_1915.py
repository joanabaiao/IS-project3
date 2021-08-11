# Generated by Django 3.1.7 on 2021-04-05 19:15

import django.core.validators
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20210405_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='language',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Drama', 'Drama'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Thriller', 'Thriller'), ('Western', 'Western')], max_length=93),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default=2021, validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2021)]),
        ),
    ]
