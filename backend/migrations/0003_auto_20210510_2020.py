# Generated by Django 3.2 on 2021-05-10 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_contact_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='addresses',
        ),
        migrations.AddField(
            model_name='address',
            name='contact',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.contact'),
            preserve_default=False,
        ),
    ]
