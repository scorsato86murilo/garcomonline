# Generated by Django 5.1.3 on 2024-11-28 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_tamanhoimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='ladodireito',
            name='texto',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ladoesquerdo',
            name='texto',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tamanhoimg',
            name='altura',
            field=models.IntegerField(default=0),
        ),
    ]
