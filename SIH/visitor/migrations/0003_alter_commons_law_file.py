# Generated by Django 4.1.11 on 2023-09-21 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0002_rename_childrenlr_children_law_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commons_law',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
