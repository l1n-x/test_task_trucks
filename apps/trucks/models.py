from django.db import models
from django.db.models import UniqueConstraint


class TruckModel(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=255,
                            blank=False, unique=True)
    weight_capacity = models.PositiveSmallIntegerField(
        verbose_name='Удельная грузоподъемность', blank=False
    )

    class Meta:
        verbose_name = 'Модель грузовика'
        verbose_name_plural = 'Модели грузовиков'

    def __str__(self):
        return self.name


class Truck(models.Model):
    number = models.CharField(verbose_name='Бортовой номер', max_length=128,
                              blank=False, unique=True)
    model = models.ForeignKey(
        verbose_name='Модель',
        related_name='trucks',
        to=TruckModel,
        on_delete=models.PROTECT,
        blank=False
    )

    class Meta:
        verbose_name = 'Грузовик'
        verbose_name_plural = 'Грузовики'

    def __str__(self):
        return self.number


class Trip(models.Model):
    truck = models.ForeignKey(
        verbose_name='Грузовик',
        related_name='trips',
        to=Truck,
        on_delete=models.CASCADE,
        blank=False
    )
    current_weight = models.PositiveSmallIntegerField(
        verbose_name='Погруженный вес', blank=False
    )
    date_started = models.DateTimeField(verbose_name='Дата начала рейса',
                                        auto_now_add=True)
    date_ended = models.DateTimeField(verbose_name='Дата окончания рейса',
                                      blank=True, null=True)

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Рейсы'
        constraints = [
            UniqueConstraint(fields=['truck', 'date_ended'],
                             name='unique_trip')
        ]

    def __str__(self):
        return f'{self.truck.number} - {self.date_started}'

    @property
    def overload(self) -> int:
        percent = int(
            self.current_weight / (self.truck.model.weight_capacity / 100)
        )

        return 0 if percent < 100 else percent - 100
