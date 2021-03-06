# Generated by Django 2.2.6 on 2019-10-24 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['title'], verbose_name='Slug')),
                ('approved_question', models.BooleanField(default=False, verbose_name='Active')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Onlince since')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
    ]
