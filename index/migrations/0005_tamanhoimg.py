# Generated by Django 5.1.3 on 2024-11-28 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_alter_nomeestabelecimento_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='TamanhoImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('altura', models.IntegerField(default=40)),
                ('largura', models.IntegerField(default=40)),
            ],
        ),
    ]