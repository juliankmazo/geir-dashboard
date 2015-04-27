from core.controllers import BaseController
from core.models import Commoditie
from core.models import Exchange
from core.models import Stock
from core.models import InterestRate
from core.helpers import QuandlHelper


class TaskUpdateInformationController(BaseController):
    # This controller is in charge of populating, getting the info
    # from quandl and saving it in the datastore
    def get(self):
        Commoditie.populate()
        Exchange.populate()
        Stock.populate()
        InterestRate.populate()
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

        stocks = Stock.query().fetch()
        for stock in stocks:
            params = QuandlHelper.get_basic_info(stock.code)
            params = QuandlHelper.get_day_variation(stock.code, params)
            params = QuandlHelper.get_month_variation(stock.code, params)
            params = QuandlHelper.get_year_variation(stock.code, params)
            if 'error' not in params:
                stock.name = params['name']
                stock.dayVariation = params['day_variation']
                stock.monthVariation = params['month_variation']
                stock.yearVariation = params['year_variation']
                stock.updated = params['last_date']
                stock.value = params['value']
                stock.put()

        interestRates = InterestRate.query().fetch()
        for interest in interestRates:
            params = QuandlHelper.get_basic_info(interest.code)
            params = QuandlHelper.get_day_variation(interest.code, params)
            params = QuandlHelper.get_month_variation(interest.code, params)
            params = QuandlHelper.get_year_variation(interest.code, params)
            if 'error' not in params:
                interest.name = params['name']
                interest.dayVariation = params['day_variation']
                interest.monthVariation = params['month_variation']
                interest.yearVariation = params['year_variation']
                interest.updated = params['last_date']
                interest.value = params['value']
                interest.put()
