
class BaseHelper():
    # This are some function used for the templates
    @classmethod
    def float2percentage(cls, number):
        return "{0:.2%}".format(number or 0)

    @classmethod
    def format_currency(cls, value):
        if value is None:
            value = 0
        return "${:,.2f}".format(value)
