# Generated by Django 4.1.11 on 2023-09-23 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0005_alter_commons_law_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='children_law',
            name='law_videos',
            field=models.FileField(blank=True, null=True, upload_to='law video'),
        ),
        migrations.AddField(
            model_name='commons_law',
            name='law_videos',
            field=models.FileField(blank=True, null=True, upload_to='law video'),
        ),
        migrations.AddField(
            model_name='mens_law',
            name='law_videos',
            field=models.FileField(blank=True, null=True, upload_to='law video'),
        ),
        migrations.AddField(
            model_name='transgender_law',
            name='law_videos',
            field=models.FileField(blank=True, null=True, upload_to='law video'),
        ),
        migrations.AddField(
            model_name='women_law',
            name='law_videos',
            field=models.FileField(blank=True, null=True, upload_to='law video'),
        ),
    ]
