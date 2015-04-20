import unittest
from google.appengine.ext import testbed
from core.helpers import QuandlHelper


class TestQuandlHeleprs(unittest.TestCase):

    def setUp(self):
        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()
        # Next, declare which service stubs you want to use.
        self.testbed.init_urlfetch_stub()

    def tearDown(self):
        self.testbed.deactivate()

    # def testLookForStock(self):
    #     data = QuandlHelper.get_data(self.STOCKS[0])
    #     code = self.STOCKS[0].split('/')[1]
    #     if data:
    #         self.assertEqual(code, data['code'])
    #     else:
    #         self.assertFalse(data)

    # def testLookForCommoditie(self):
    #     for commoditie in self.COMMODITIES:
    #         data = QuandlHelper.get_data(commoditie)
    #         code = commoditie.split('/')[1]
    #         if data:
    #             self.assertEqual(code, data['code'])
    #         else:
    #             self.assertFalse(data)

    # def testLookForExchanges(self):
    #     for exchange in self.EXCHANGE_RATES:
    #         data = QuandlHelper.get_data(exchange)
    #         code = exchange.split('/')[1]
    #         if data:
    #             self.assertEqual(code, data['code'])
    #         else:
    #             self.assertFalse(data)

    # def testBasicInfoForCommoditie(self):
    #     for commoditie in self.COMMODITIES:
    #         params = QuandlHelper.get_basic_info(commoditie)
    #         if 'error' in params:
    #             print params['error']
    #             self.assertEquals('No data was returned from Quandl',
    #                               params['error'])
    #         else:
    #             print params['code']
    #             print params['name']
    #             print params['last_date']
    #             print '------'
    #             code = commoditie.split('/')[1]
    #             self.assertEqual(code, params['code'])

    # def testBasicInfoForExchanges(self):
    #     for exchange in self.EXCHANGE_RATES:
    #         params = QuandlHelper.get_basic_info(exchange)
    #         if 'error' in params:
    #             print exchange
    #             print params['error']
    #             print '------'
    #             self.assertEquals('No data was returned from Quandl',
    #                               params['error'])
    #         else:
    #             print params['code']
    #             print params['name']
    #             print params['last_date']
    #             print '------'
    #             code = exchange.split('/')[1]
    #             self.assertEqual(code, params['code'])

    def testDayVariationForCommoditie(self):
        for commoditie in self.COMMODITIES:
            params = QuandlHelper.get_day_variation(commoditie)
            if 'error' in params:
                print params['error']
                self.assertEquals('No data was returned from Quandl',
                                  params['error'])
            else:
                print commoditie
                print params['column_names']
                print params['day_variation']
                print '------'
                self.assertTrue(isinstance(params['day_variation'], float))

    def testDayVariationForExchange(self):
        for exchange in self.EXCHANGE_RATES:
            params = QuandlHelper.get_day_variation(exchange)
            if 'error' in params:
                print params['error']
                self.assertEquals('No data was returned from Quandl',
                                  params['error'])
            else:
                print exchange
                print params['column_names']
                print params['day_variation']
                print '------'
                self.assertTrue(isinstance(params['day_variation'], float))

    STOCKS = ['YAHOO/INDEX_GSPC']
    COMMODITIES = ['CHRIS/ICE_T1',      # WTI Crude Oil Price
                   'OFDP/FUTURE_C1',    # Corn
                   'OFDP/FUTURE_SB1',   # Sugar
                   'OFDP/COPPER_6',     # Copper
                   'YAHOO/TSX_XGD_TO',  # Gold
                   'OFDP/FUTURE_B1',    # Brent Crude
                   'OFDP/FUTURE_W1',    # Wheat
                   'OFDP/FUTURE_KC1',   # Coffee
                   'OFDP/ALUMINIUM_21', # Aluminium
                   'LBMA/SILVER',       # Silver
                   'CHRIS/CME_NG1',     # Natural Gas
                   'OFDP/FUTURE_S1',    # Soybean
                   'OFDP/FUTURE_CT1',   # Cutton
                   'OFDP/NICKEL_41',    # Nickel
                   'JOHNMATT/PLAT',     # Platinum
                   'OFDP/FUTURE_RB1',   # Gasoline
                   'OFDP/FUTURE_RR1',   # Rice
                   'OFDP/FUTURE_CC1',   # Cocoa
                   'OFDP/STEELBILLET_46',# Steel
                   'JOHNMATT/PALL'      # Palladium
                   ]
    EXCHANGE_RATES = ['CURRFX/USDAUD',
                      'CURRFX/USDBRL',
                      'CURRFX/USDGBP',
                      'CURRFX/USDCAD',
                      'CURRFX/USDCNY',
                      'CURRFX/USDDKK',
                      'CURRFX/USDEUR',
                      'CURRFX/USDHKD',
                      'CURRFX/USDINR',
                      'CURRFX/USDJPY',
                      'CURRFX/USDMYR',
                      'CURRFX/USDMXN',
                      'CURRFX/USDTWD',
                      'CURRFX/USDNZD',
                      'CURRFX/USDNOK',
                      'CURRFX/USDSGD',
                      'CURRFX/USDZAR',
                      'CURRFX/USDKRW',
                      'CURRFX/USDLKR',
                      'CURRFX/USDSEK',
                      'CURRFX/USDCHF',
                      'CURRFX/USDTHB',
                      'garbage'
                      ]

if __name__ == '__main__':
    unittest.main()
