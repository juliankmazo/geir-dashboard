
class BaseHelper():

    @classmethod
    def float2percentage(cls, number):
        return "{0:.2f}%".format(number)

    @classmethod
    def format_currency(cls, value):
        if value is None:
            value = 0
        return "${:,.0f}".format(value)
