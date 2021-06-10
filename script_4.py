
from datetime import datetime,timedelta
import csv
from tapi_yandex_metrika import YandexMetrikaStats
from config import token

ACCESS_TOKEN = token
COUNTER_ID = "22428703"

client = YandexMetrikaStats(access_token=ACCESS_TOKEN)

today = datetime.today().date()
start_day = datetime.today().date() - timedelta(days=29)

params = dict(
    ids=COUNTER_ID,
    date1=str(start_day),
    date2=str(today),
    metrics="ym:s:pageviews",
    dimensions="ym:s:publisherArticleTitle",
    sort="-ym:s:pageviews",
    filters="ym:pv:URLDomain == 'vostokmedia.com'",
    limit=10
    # Other params -> https://yandex.ru/dev/metrika/doc/api2/api_v1/data.html
)
report = client.stats().get(params=params)
rows = report().to_values()
info = [params['date1'],params['date2']]
columns = ['Заголовки','Просмотры']
segment = [params['filters'].split('==')[1]]

params_search = dict(
    ids=COUNTER_ID,
    date1=str(start_day),
    date2=str(today),
    metrics="ym:s:pageviews",
    dimensions="ym:s:publisherArticleTitle",
    sort="-ym:s:pageviews",
    filters="ym:s:lastSearchEngine == 'Переходы из поисковых систем'",
    limit=10
    # Other params -> https://yandex.ru/dev/metrika/doc/api2/api_v1/data.html
)

report_search = client.stats().get(params=params_search)
rows_search = report_search().to_values()
segment_search = [params_search['filters'].split('==')[1]]

params_google = dict(
    ids=COUNTER_ID,
    date1=str(start_day),
    date2=str(today),
    metrics="ym:s:pageviews",
    dimensions="ym:s:publisherArticleTitle",
    sort="-ym:s:pageviews",
    filters="ym:s:lastRecommendationSystem == 'Google Discover'",
    limit=10
    # Other params -> https://yandex.ru/dev/metrika/doc/api2/api_v1/data.html
)

report_google = client.stats().get(params=params_google)
rows_google = report_google().to_values()
segment_google = [params_google['filters'].split('==')[1]]




with open("data_script_4.csv", 'w+',newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(info)
    writer.writerow(segment)
    writer.writerow(columns)
    writer.writerows(rows)
    writer.writerow('')
    writer.writerow(segment_search)
    writer.writerows(rows_search)
    writer.writerow('')
    writer.writerow(segment_google)
    writer.writerows(rows_google)
