# Generated by Django 4.2.7 on 2023-12-04 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_alter_topic_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
