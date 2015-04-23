
class BaseHelper():

    @classmethod
    def float2percentage(cls, number):
        if not number:
            number = 0
        return "{0:.2f}%".format(number*100)

    @classmethod
    def format_currency(cls, value):
        if value is None:
            value = 0
        return "${:,.2f}".format(value)
