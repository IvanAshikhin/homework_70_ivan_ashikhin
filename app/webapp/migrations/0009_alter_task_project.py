# Generated by Django 4.1.7 on 2023-04-17 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_project_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='project', to='webapp.project', verbose_name='Проект'),
        ),
    ]
