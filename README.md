# Модификация [Кошачьего благотворительного фонда](https://github.com/SowaSova/cat_charity_fund)

Реализована возможность формирования отчета в гугл-таблице.
Таблица содержит все закрытые проекты, отсортированные по скорости сбора средств - от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму.

Для запуска проекта:

```
git clone git@github.com:SowaSova/cat_charity_fund.git
cd cat_charity_fund
```
win:
```
python -m venv venv
. venv/Scripts/activate
```
*nix:
```
python3 -m venv venv
. venv/bin/activate
```

```
pip install -r requirements.txt
```
```
uvicorn app.main:app --reload
```
>[Документация](http://localhost:8000/docs)
