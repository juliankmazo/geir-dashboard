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
    def get_basic_info(cls, code, params={}):
        if code:
            fromDate = '&trim_start=' + cls.TODAY.strftime('%Y-%m-%d')
            data = cls.get_data(code, fromDate)
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
        response = urlfetch.fetch(endpoint, deadline=7)
        if response.status_code == 200:
            data = json.loads(response.content)
            # print('Code: ' + str(data['code']) + '...' + str(data['column_names']))
            return data
        else:
            return False

    @classmethod
    def get_day_variation(cls, code, params={}):
        if code:
            fromDate = '&trim_start=' + cls.YESTERDAY.strftime('%Y-%m-%d')
            data = cls.get_data(code, fromDate)
            if data:
                # print data['data'][0][0], data['data'][0][1]
                # print data['data'][1][0], data['data'][1][1]
                params['value'] = data['data'][0][1]
                params['day_variation'] = float(data['data'][0][1])/float(data['data'][1][1]) - 1.0
                params['column_names'] = data['column_names']
            else:
                params['error'] = 'No data was returned from Quandl'
            return params

    @classmethod
    def get_month_variation(cls, code, params={}):
        if code:
            fromDate = '&trim_start=' + cls.MONTH_AGO.strftime('%Y-%m-%d')
            data = cls.get_data(code, fromDate)
            if data:
                last_day = len(data['data']) - 1
                # print data['data'][last_day][0], data['data'][last_day][1]
                params['month_variation'] = float(data['data'][0][1])/float(data['data'][last_day][1]) - 1.0
                params['column_names'] = data['column_names']
            else:
                params['error'] = 'No data was returned from Quandl'
            return params

    @classmethod
    def get_year_variation(cls, code, params={}):
        if code:
            fromDate = '&trim_start=' + cls.YEAR_AGO.strftime('%Y-%m-%d')
            data = cls.get_data(code, fromDate)
            if data:
                last_day = cls.get_valid_last_day(data)
                # print data['data'][last_day][0], data['data'][last_day][1]
                params['year_variation'] = float(data['data'][0][1])/float(data['data'][last_day][1]) - 1.0
                params['column_names'] = data['column_names']
            else:
                params['error'] = 'No data was returned from Quandl'
            return params

    @classmethod
    def get_valid_last_day(cls, data):
        last_day = len(data['data']) - 1
        while not data['data'][last_day][1]:
            last_day -= 1
        return last_day
