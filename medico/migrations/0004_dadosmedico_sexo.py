# Generated by Django 5.1.4 on 2025-01-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0003_alter_dadosmedico_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadosmedico',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
