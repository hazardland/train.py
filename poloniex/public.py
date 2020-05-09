from urllib import request
from datetime import datetime

class InvalidPeriond(Exception):
    pass

def returnChartData(currencyPair, start, end, period=300):
    if period not in (300, 900, 1800, 7200, 14400, 86400):
        raise InvalidPeriond

    if isinstance(start, str):
        start = int(datetime.strptime(start, '%Y-%m-%d %H:%M:%S').timestamp())

    if isinstance(end, str):
        end = int(datetime.strptime(end, '%Y-%m-%d %H:%M:%S').timestamp())

    url = ('https://poloniex.com/public?command=returnChartData'
           '&currencyPair=%s'
           '&start=%s'
           '&end=%s'
           '&period=%s'
           %
           (currencyPair, start, end, period))
    print(url)
    result = request.urlopen(url)
    print(result.peek())
    return result
