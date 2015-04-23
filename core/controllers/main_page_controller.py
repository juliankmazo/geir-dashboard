from core.controllers import BaseController
from core.models import Commoditie
from core.models import Exchange
from core.models import Stock
from core.models import InterestRate


class MainPageController(BaseController):

    def get(self):
        commodities = Commoditie.query().order(Commoditie.code).fetch()
        exchanges = Exchange.query().order(Exchange.code).fetch()
        stocks = Stock.query().order(Stock.code).fetch()
        interests = InterestRate.query().order(InterestRate.code).fetch()
        self.render('main_page.html', commodities=commodities,
                    exchanges=exchanges, stocks=stocks, interests=interests)
