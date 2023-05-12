# Generated by Django 4.2.1 on 2023-05-12 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TruckModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Наименование')),
                ('weight_capacity', models.PositiveSmallIntegerField(verbose_name='Удельная грузоподъемность')),
            ],
            options={
                'verbose_name': 'Модель грузовика',
                'verbose_name_plural': 'Модели грузовиков',
            },
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=128, unique=True, verbose_name='Бортовой номер')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='trucks', to='trucks.truckmodel', verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Грузовик',
                'verbose_name_plural': 'Грузовики',
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_weight', models.PositiveSmallIntegerField(verbose_name='Погруженный вес')),
                ('overload', models.PositiveSmallIntegerField(default=0, verbose_name='Перегруз (в %)')),
                ('date_started', models.DateTimeField(auto_now_add=True, verbose_name='Дата начала рейса')),
                ('date_ended', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания рейса')),
                ('truck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='trucks.truck', verbose_name='Грузовик')),
            ],
            options={
                'verbose_name': 'Рейс',
                'verbose_name_plural': 'Рейсы',
            },
        ),
        migrations.AddConstraint(
            model_name='trip',
            constraint=models.UniqueConstraint(fields=('truck', 'date_ended'), name='unique_trip'),
        ),
    ]
