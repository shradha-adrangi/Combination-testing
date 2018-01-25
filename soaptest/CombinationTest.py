import unittest

class CombinationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.environment = 'c1-staging'
        cls.api_key = 'qa_universal_api_key'
        cls.customer_code = 'QE4P'
        cls.entity_Code = '3000'