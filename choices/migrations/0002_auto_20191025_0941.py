# Generated by Django 2.2.6 on 2019-10-25 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'ordering': ['-created_at'], 'verbose_name': 'Choice Manager', 'verbose_name_plural': 'Choices Manager'},
        ),
    ]
