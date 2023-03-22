import os
import logging
import pytest
import pandas as pd

logging.basicConfig(
    filename="logs/test.log",
    level=logging.INFO,
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s")

@pytest.fixture(name="test_import")
def test_import():
    """
    import all the dataframe
    """
    try:
        customers_df = pd.read_csv("./data/customers_dataset.csv")
        orders_df = pd.read_csv("./data/orders_dataset")
        order_items_df = pd.read_csv("./data/order_items_dataset")
        geolocation_df = pd.read_csv("./data/geolocation_dataset.csv")
        order_payments_df = pd.read_csv("./data/order_payments_dataset.csv")
        order_reviews_df = pd.read_csv("./data/order_reviews_dataset.csv")
        products_df = pd.read_csv("./data/products_dataset.csv")
        product_category_name_translation_df = pd.read_csv("./data/product_category_name_translation.csv")
        sellers_df = pd.read_csv("./data/sellers_dataset.csv")
        
        logging.info("Testing import_data: SUCCESS")
    except FileNotFoundError as err:
        logging.error("Testing import_data: The file wasn't found")
        raise err
    return customers_df, orders_df, order_items_df, order_payments_df

