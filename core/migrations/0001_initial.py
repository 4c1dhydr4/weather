# Generated by Django 4.1.2 on 2022-10-12 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre', max_length=140, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(editable=False, help_text='Timestamp', verbose_name='Timestamp')),
                ('temperature', models.DecimalField(decimal_places=2, help_text='Temperature Record', max_digits=6, verbose_name='Temperature')),
                ('description', models.CharField(help_text='Nombre', max_length=140, verbose_name='Nombre')),
                ('icon', models.CharField(help_text='Open Weather Icon Code', max_length=4, verbose_name='Icon')),
                ('city', models.ForeignKey(editable=False, help_text='City', on_delete=django.db.models.deletion.CASCADE, to='core.city', verbose_name='City')),
            ],
        ),
    ]