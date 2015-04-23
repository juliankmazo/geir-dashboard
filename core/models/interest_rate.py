from core.models import BaseModel


class InterestRate(BaseModel):

    @classmethod
    def populate(cls):
        for i in cls.INTEREST_RATES:
            interest_rate = InterestRate.query(InterestRate.code == i[0]).get()
            if not interest_rate:
                new_interest_rate = InterestRate(code=i[0], column=i[1])
                new_interest_rate.put()

    INTEREST_RATES = [['FRED/DTB4WK', 1],
                      ['FRED/DTB3', 1],
                      ['FRED/DTB6', 1],
                      ['FRED/DTB1YR', 1],
                      ['FRED/DGS2', 1],
                      ['FRED/DGS10', 1],
                      ['FRED/DGS30', 1]
                      ]
