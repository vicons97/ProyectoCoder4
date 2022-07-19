# Generated by Django 4.0.6 on 2022-07-19 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Familia', '0002_alter_familia_altura'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amigos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('altura', models.FloatField()),
                ('fecha_de_nacimiento', models.DateField(max_length=50)),
            ],
        ),
    ]