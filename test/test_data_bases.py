import unittest
from google.appengine.ext import testbed
from google.appengine.ext import ndb
from core.models import Commoditie
from core.models import Exchange
from core.controllers import TaskUpdateInformationController


class TestDataBases(unittest.TestCase):

    def setUp(self):
        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()
        # Next, declare which service stubs you want to use.
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        self.testbed.init_urlfetch_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def testPopulateCommodities(self):
        lenCommodities = len(Commoditie.COMMODITIES)
        queryCommodities = Commoditie.query().fetch()
        self.assertEquals(0, len(queryCommodities))
        Commoditie.populate()
        queryCommodities = Commoditie.query().fetch()
        self.assertEquals(lenCommodities, len(queryCommodities))

    def testPopulateExchages(self):
        lenExchanges = len(Exchange.EXCHANGE_RATES)
        queryExchanges = Exchange.query().fetch()
        self.assertEquals(0, len(queryExchanges))
        Exchange.populate()
        queryExchanges = Exchange.query().fetch()
        self.assertEquals(lenExchanges, len(queryExchanges))

    def testTaskUpdateInformation(self):
        lenExchanges = len(Exchange.EXCHANGE_RATES)
        lenCommodities = len(Commoditie.COMMODITIES)

        queryExchanges = Exchange.query().fetch()
        queryCommodities = Commoditie.query().fetch()

        self.assertEquals(0, len(queryExchanges))
        self.assertEquals(0, len(queryCommodities))

        TaskUpdateInformationController.get()

        queryExchanges = Exchange.query().fetch()
        queryCommodities = Commoditie.query().fetch()

        self.assertEquals(lenExchanges, len(queryExchanges))
        self.assertEquals(lenCommodities, len(queryCommodities))

if __name__ == '__main__':
    unittest.main()
