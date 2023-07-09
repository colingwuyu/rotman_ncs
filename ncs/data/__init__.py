import os
import pandas as pd

from ncs.data.downloader import download_and_extract


def data_folder():
    # Get the home directory
    if os.name == 'nt':  # For Windows
        base_dir = os.getenv('APPDATA')
    else:  # For Linux/OS X
        base_dir = os.path.expanduser('~')

    dest_dir = os.path.join(base_dir, 'rotman_ncs_data', 'ncs_data')

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    return dest_dir


def check_data_exist_and_download(data_file):
    if not os.path.exists(data_file):
        download_and_extract(
            'https://storage.googleapis.com/rotman-ncs-data-buket/ncs_data.zip', 'rotman_ncs_data')


def load_stock_returns_on_calls(data_type='train'):
    data_file = f'{data_folder()}/{data_type}/stock_return_data.parquet'
    check_data_exist_and_download(data_file)
    return pd.read_parquet(data_file)


def load_stock_history():
    data_file = f'{data_folder()}/all_stock_price_history.parquet'
    check_data_exist_and_download(data_file)
    return pd.read_parquet(data_file)


def load_call_description(data_type='train'):
    data_file = f'{data_folder()}/{data_type}/call_data.parquet'
    check_data_exist_and_download(data_file)
    return pd.read_parquet(data_file)


def load_call_statements(data_type='train'):
    data_file = f'{data_folder()}/{data_type}/call_statement_data.parquet'
    check_data_exist_and_download(data_file)
    return pd.read_parquet(data_file)
