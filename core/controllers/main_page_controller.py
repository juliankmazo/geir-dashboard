from core.controllers import BaseController
from core.models import Commoditie
from core.models import Exchange


class MainPageController(BaseController):

    def get(self):
        commodities = Commoditie.query().fetch()
        exchanges = Exchange.query().fetch()
        self.render('main_page.html', commodities=commodities,
                    exchanges=exchanges)
