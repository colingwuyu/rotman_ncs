import os
import unittest
from tempfile import TemporaryDirectory as tempdir
from ncs.call_strategy.strategy import run_strategy


cur_dir = os.path.dirname(os.path.abspath(__file__))


class TestRunStrategy(unittest.TestCase):
    def test_random_strategy(self):
        with tempdir() as tmp:
            run_strategy(
                action_file=f'{cur_dir}/../ncs/call_strategy/random_action.csv',
                holding_period=1,
                log_file='',
                save_portfolio_path='portfolio.parquet')
            self.assertTrue(os.path.exists('portfolio.parquet'))


if __name__ == '__main__':
    unittest.main()
