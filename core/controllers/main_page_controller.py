from core.controllers import BaseController
from core.models import Commoditie
from core.models import Exchange
from core.models import Stock
from core.models import InterestRate


class MainPageController(BaseController):
    # Main page controller. We get all the objects in the database
    # and then we render all in the mainpage template
    def get(self):
        commodities = Commoditie.query().order(Commoditie.code).fetch()
        exchanges = Exchange.query().order(Exchange.code).fetch()
        stocks = Stock.query().order(Stock.code).fetch()
        interests = InterestRate.query().order(InterestRate.code).fetch()
        self.render('main_page.html', commodities=commodities,
                    exchanges=exchanges, stocks=stocks, interests=interests)
