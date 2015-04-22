from core.controllers import BaseController
from core.models import Commoditie
from core.models import Exchange
from core.helpers import QuandlHelper


class TaskUpdateInformationController(BaseController):

    def get(self):
        Commoditie.populate()
        Exchange.populate()
        commodities = Commoditie.query().fetch()
        for commoditie in commodities:
            params = QuandlHelper.get_basic_info(commoditie.code)
            params = QuandlHelper.get_day_variation(commoditie.code, params)
            params = QuandlHelper.get_month_variation(commoditie.code, params)
            params = QuandlHelper.get_year_variation(commoditie.code, params)
            if 'error' not in params:
                commoditie.name = params['name']
                commoditie.dayVariation = params['day_variation']
                commoditie.monthVariation = params['month_variation']
                commoditie.yearVariation = params['year_variation']
                commoditie.updated = params['last_date']
                commoditie.value = params['value']
                commoditie.put()

        exchanges = Exchange.query().fetch()
        for exchange in exchanges:
            params = QuandlHelper.get_basic_info(exchange.code)
            params = QuandlHelper.get_day_variation(exchange.code, params)
            params = QuandlHelper.get_month_variation(exchange.code, params)
            params = QuandlHelper.get_year_variation(exchange.code, params)
            if 'error' not in params:
                exchange.name = params['name']
                exchange.dayVariation = params['day_variation']
                exchange.monthVariation = params['month_variation']
                exchange.yearVariation = params['year_variation']
                exchange.updated = params['last_date']
                exchange.value = params['value']
                exchange.put()
