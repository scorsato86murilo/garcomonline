# Generated by Django 5.1.3 on 2024-11-28 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_ladodireito_background'),
    ]

    operations = [
        migrations.CreateModel(
            name='TituloPagina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='Bem Vindo!', max_length=70)),
            ],
        ),
    ]
