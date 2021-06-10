#https://api-metrika.yandex.net/stat/v1/data.csv?

import csv

from tapi_yandex_metrika import YandexMetrikaStats
from config import token

ACCESS_TOKEN = token
COUNTER_ID = "22428703"

client = YandexMetrikaStats(access_token=ACCESS_TOKEN)

params = dict(
    ids=COUNTER_ID,
    date1="2020-05-01",
    date2="2020-05-31",
    metrics="ym:s:goal32666421users",
    dimensions="ym:s:startURLDomain"
    # Other params -> https://yandex.ru/dev/metrika/doc/api2/api_v1/data.html
)
report = client.stats().get(params=params)
rows = report().to_values()
date = [params['date1'],params['date2']]
columns = ['Стартовый Домен Входа','Уникальные пользователи совершившие цель: 1-ый автодоскрол']

totals = []
for key in report.data.keys():
    if key == 'totals':
        totals.append(key)
        value = report[key].pop()
        totals.append(value)

with open("data.csv", 'w+',newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(date)
    writer.writerow(columns)
    writer.writerows(rows)
    writer.writerow(totals)