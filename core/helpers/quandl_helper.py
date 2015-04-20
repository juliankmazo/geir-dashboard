from core.helpers import BaseHelper
from google.appengine.api import urlfetch
import json
import datetime


class QuandlHelper(BaseHelper):
    NAME_EXTENSION = '.json?auth_token=iZKVyFSQgRbD18CcEjJC'
    URL = 'http://www.quandl.com/api/v1/datasets/'
    TODAY = datetime.datetime.now()
    YESTERDAY = TODAY + datetime.timedelta(days=-10)
    MONTH_AGO = TODAY + datetime.timedelta(days=-30)
    YEAR_AGO = TODAY + datetime.timedelta(days=-365)

    @classmethod
    def get_basic_info(cls, code):
        if code:
            fromDate = '&trim_start=' + cls.TODAY.strftime('%Y-%m-%d')
            data = cls.get_data(code, fromDate)
            params = {}
            if data:
                params['name'] = data['name']
                params['code'] = data['code']
                params['last_date'] = data['to_date']
            else:
                params['error'] = 'No data was returned from Quandl'
            return params

    @classmethod
    def get_data(cls, code, fromDate=None):
        if fromDate:
            endpoint = cls.URL + code + cls.NAME_EXTENSION + fromDate
        else:
            endpoint = cls.URL + code + cls.NAME_EXTENSION
        response = urlfetch.fetch(endpoint)
        if response.status_code == 200:
            data = json.loads(response.content)
            # print('Code: ' + str(data['code']) + '...' + str(data['column_names']))
            return data
        else:
            return False

    @classmethod
    def get_day_variation(cls, code):
        if code:
            fromDate = '&trim_start=' + cls.YESTERDAY.strftime('%Y-%m-%d')
            data = cls.get_data(code, fromDate)
            params = {}
            if data:
                print data['data'][0][1]
                print data['data'][1][1]
                params['day_variation'] = float(data['data'][0][1])/float(data['data'][1][1]) - 1.0
                params['column_names'] = data['column_names']
            else:
                params['error'] = 'No data was returned from Quandl'
            return params
