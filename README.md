# Аналитика в компании

В данном репозитории представлен проект, в котором продемонстрированы базовые задачи, с которыми может столкнуться Junior Data Analyst.
Представим, что мы устроились в стартап, объединяющий в себе ленту новостей и мессенджинг, нам нужно настроить аналитические процессы внутри нашей компании.

---

1. [**Формирование отчета по ключевым метрикам в телеграм**](https://github.com/BorisloveeeeZ/analyst_cycle/blob/main/telegram_bot.py): 

Аналитика начинается с вопроса ***сколько?***. Сколько пользователей пользуются нашим приложением в день, сколько они ставят лайков, какой CTR, сколько просмотров итд. Мы всегда должны получить быстрый ответ на ключевые вопросы, сформируем отчет и настроим автоматическое расписание(чтобы он приходил к нам каждое утро без нашего участия). 

***Стек:*** Pandas, seaborn,[**CI/CD**](https://github.com/BorisloveeeeZ/analyst_cycle/blob/main/gitlab-ci.yml), matplotlib, telegram, pandahouse, os, 
[***Пример отчета***](https://sun1-92.userapi.com/s/v1/if2/j985FZZhVNvKl7FnCPoB10WYhQMCjOFV1MJyCrGZnb-xsK_WdpUEWwZQADW773zc8mwZ65xQSRmpJflz-Jy_rXUa.jpg?size=972x2160&quality=95&type=album)

---

2. [**Что делать, если что-то пошло не так?**]:

Как понять и быстро среагировать на изменения метрики, если что-то пошло не так? Для этого мы сделаем ***систему оповещений***, чтобы аллерт приходил к нам, когда случается аномальный рост или падение

Стек: Pandas, SQL, Tableau.

---

3. [**Анализируем продуктовые метрики**](https://github.com/BorisloveeeeZ/analyst_cycle/blob/main/product.ipynb)

С первостепенными задачами разобрались, теперь нужно углубиться в продукт, чтобы исследовать различные гипотезы. Ответим на более сложные продуктовые вопросы
А так же решим задачу проджекта-Васи [**E-commerce работы с RFM сегментацией**](https://gitlab.com/BorisloveeeZ/analyst_cycle/-/blob/main/rfm_cohort.ipynb)
Стек: SQL, matplotlib, seaborn, pandas.

---

4. [**A/B тестирование**](https://github.com/BorisloveeeeZ/analyst_cycle/blob/main/A_B.ipynb)

Дата-сайентисты пришли к нам с новым алгоритмом рекомендаций, они считают что он увеличит наш CTR. 
Проведем исследование, является ли алгоритм удачным и сделаем вывод.


Стек: Pandas, matplotlib, seaborn, numpy.

---
5. [**Work with requests**](https://github.com/BorisloveeeeZ/analyst_cycle/blob/main/python_core_train/requests.py)

Пример работы с Api. Консольная утилита, которая сокращает ссылку в битлинк, если она уже создана, считает клики по ней.


Стек: requests, os, urllib.

---
