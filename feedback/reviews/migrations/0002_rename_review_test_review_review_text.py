# Generated by Django 4.0.3 on 2022-04-04 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review_test',
            new_name='review_text',
        ),
    ]