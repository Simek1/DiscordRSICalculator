import unittest
from RSI_calculator import calculate_RSI
import time
import pandas as pd


class TestRSICalculation(unittest.TestCase):

    def test_rsi_calculation_high_rsi(self):
        # Test for RSI calculation when RSI is above 70
        data = {"timestamp" : ['1970-01-01 00:28:38.467202', '1970-01-01 00:28:38.467203', '1970-01-01 00:28:38.467204', '1970-01-01 00:28:38.467205', '1970-01-01 00:28:38.467206', 
                           '1970-01-01 00:28:38.467207','1970-01-01 00:02:51.846720800','1970-01-01 00:28:38.467210','1970-01-01 00:00:00.171846720',
                           '1970-01-01 00:28:38.467212', '1970-01-01 00:28:38.467214', '1970-01-01 00:28:38.467216', '1970-01-01 00:28:38.467218', '1970-01-01 00:28:38.467220',
                           '1970-01-01 00:28:38.467222'],
                 "closing_prices": [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]}
        df = pd.DataFrame(columns=["close"])
        for i in range(len(data["timestamp"])):
            df.loc[data["timestamp"][i]] = data["closing_prices"][i]
        rsi = calculate_RSI(df)
        self.assertTrue(rsi > 70)

    def test_rsi_calculation_low_rsi(self):
        # Test for RSI calculation when RSI is below 30
        data = {"timestamp" : ['1970-01-01 00:28:38.467202', '1970-01-01 00:28:38.467203', '1970-01-01 00:28:38.467204', '1970-01-01 00:28:38.467205', '1970-01-01 00:28:38.467206', 
                           '1970-01-01 00:28:38.467207','1970-01-01 00:02:51.846720800','1970-01-01 00:28:38.467210','1970-01-01 00:00:00.171846720',
                           '1970-01-01 00:28:38.467212', '1970-01-01 00:28:38.467214', '1970-01-01 00:28:38.467216', '1970-01-01 00:28:38.467218', '1970-01-01 00:28:38.467220',
                           '1970-01-01 00:28:38.467222'],
                 "closing_prices": [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16]}
        df = pd.DataFrame(columns=["close"])
        for i in range(len(data["timestamp"])):
            df.loc[data["timestamp"][i]] = data["closing_prices"][i]
        rsi = calculate_RSI(df)
        self.assertTrue(rsi < 30)


if __name__ == '__main__':
    unittest.main()

