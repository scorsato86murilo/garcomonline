# Generated by Django 5.1.3 on 2024-11-27 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LadoDireito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.CharField(default='#FFFFFF', max_length=7)),
                ('estilo_letra_titulo', models.CharField(default='Arial, sans-serif', max_length=100)),
                ('cor_letra_titulo', models.CharField(default='#333333', max_length=7)),
                ('estilo_letra_texto', models.CharField(default='Arial, sans-serif', max_length=100)),
                ('cor_letra_texto', models.CharField(default='#000000', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='LadoEsquerdo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.CharField(default='#FFFFFF', max_length=7)),
                ('estilo_letra_titulo', models.CharField(default='Arial, sans-serif', max_length=100)),
                ('cor_letra_titulo', models.CharField(default='#000000', max_length=7)),
                ('estilo_letra_texto', models.CharField(default='Arial, sans-serif', max_length=100)),
                ('cor_letra_texto', models.CharField(default='#333333', max_length=7)),
            ],
        ),
    ]
