import requests


def http_request():
    response = requests.get(
        'http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json')
    last_twenty_years = response.json()[1][:20]
    for year in last_twenty_years:
        # print(year)
        if year['value']:
            display_width = year["value"] // 10_000_000
            print(f"{year['date']}: {year['value']}", "=" * display_width)
    print(last_twenty_years)


if __name__ == '__main__':
    http_request()
