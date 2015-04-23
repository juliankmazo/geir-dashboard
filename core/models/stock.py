from core.models import BaseModel


class Stock(BaseModel):

    @classmethod
    def populate(cls):
        for s in cls.STOCK:
            stock = Stock.query(Stock.code == s[0]).get()
            if not stock:
                new_stock = Stock(code=s[0], column=s[1])
                new_stock.put()

    STOCK = [['YAHOO/INDEX_GSPC', 1]]
