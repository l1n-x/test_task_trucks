<h2>Дано:</h2>
На маршруте находится 3 грузовика с бортовыми номерами "101", "102", "К103".
"101" и "102" грузовики модели "УАЗ", а "К103" - "Камаз". 
У моделей "УАЗ" максимальная грузоподъёмность 1200 кг, а у "Камаз" - 1100 кг.
На текущий момент "101" грузовик везёт 1000 кг груза, "102" - 1250 кг, "К103" 1200 кг.

<h2>Стек:</h2>
- Приложение - Django
- СУБД - sqlite

<h2>Задача:</h2>
Создать модели под описанные объекты. 
Учесть что в систему в будущем могут добавляться новые грузовики и модели грузовиков.
Создать страницу. Добавить выпадающий список (select) для выбора модели грузовика и кнопку "Применить".
Список должен включать пункт "Все", а также все модели из справочника моделей.
Ниже разместить таблицу, отображающую справочные параметры грузовиков, 
и текущее значение перегруза в % (выводить на сколько превышена максимальная грузоподъемность).

<h3>Пример:</h3>

| Модель: | Все V | Применить |
|---------|-------|-----------|


| Борт. № | Модель | макс. грузоподъемность | текущий вес | перегруз, % |
|---------|--------|------------------------|-------------|-------------|
| 101     | Камаз  | 1100                   | 120         | 9%          |

При нажатии на "Применить" страница перезагружается, список грузовиков 
фильтруется по выбранной модели. Если выбран пункт все - выводятся грузовики всех моделей.