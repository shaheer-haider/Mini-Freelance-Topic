# Generated by Django 4.2.7 on 2023-12-04 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_topic_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
