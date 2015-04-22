from core.models import BaseModel


class Exchange(BaseModel):

    @classmethod
    def populate(cls):
        for e in cls.EXCHANGE_RATES:
            exchange = Exchange.query(Exchange.code == e[0]).get()
            if not exchange:
                new_exchange = Exchange(code=e[0], column=e[1])
                new_exchange.put()

    EXCHANGE_RATES = [['CURRFX/USDAUD', 1],
                      ['CURRFX/USDBRL', 1],
                      ['CURRFX/USDGBP', 1],
                      ['CURRFX/USDCAD', 1],
                      ['CURRFX/USDCNY', 1],
                      ['CURRFX/USDDKK', 1],
                      ['CURRFX/USDEUR', 1],
                      ['CURRFX/USDHKD', 1],
                      ['CURRFX/USDINR', 1],
                      ['CURRFX/USDJPY', 1],
                      ['CURRFX/USDMYR', 1],
                      ['CURRFX/USDMXN', 1],
                      ['CURRFX/USDTWD', 1],
                      ['CURRFX/USDNZD', 1],
                      ['CURRFX/USDNOK', 1],
                      ['CURRFX/USDSGD', 1],
                      ['CURRFX/USDZAR', 1],
                      ['CURRFX/USDKRW', 1],
                      ['CURRFX/USDLKR', 1],
                      ['CURRFX/USDSEK', 1],
                      ['CURRFX/USDCHF', 1],
                      ['CURRFX/USDTHB', 1]
                      ]
