from main import calculate_total
import pytest
import sys


def test_all_items():
    records = [
        {'name': 'Apples', 'price': 1.99, 'type': 'Wic Eligible food'},
        {'name': 'Shirt', 'price': 19.99, 'type': 'Clothing'},
        {'name': 'Book', 'price': 9.99, 'type': 'Everything else'},
        {'name': 'Fox Fur Coat', 'price': 1984.99, 'type': 'Clothing'},
    ]
    assert calculate_total('NJ', records) == 2148.63
    assert calculate_total('PA', records) == 2017.56
    assert calculate_total('DE', records) == 2016.96


# testing empty lists
def test_no_items():
    assert calculate_total('NJ', []) == 0
    assert calculate_total('PA', []) == 0
    assert calculate_total('DE', []) == 0


# testing incorrect types
def test_diff_types():
    records = [
        {'name': 'Speaker', 'price': 199.99, 'type': 'Electronic'},
        {'name': 'Laptop', 'price': 1999.99, 'type': 'awefawefg'},
        {'name': 'Amazon Echo', 'price': 49.99, 'type': 'casergrgc'},
    ]
    assert calculate_total('NJ', records) == 2398.47
    assert calculate_total('PA', records) == 2384.97
    assert calculate_total('DE', records) == 2249.97


# testing negative prices
def test_negative_prices():
    records = [
        {'name': 'speaker', 'price': -149.99, 'type': 'Electronic'},
        {'name': 'laptop', 'price': 1999.99, 'type': 'Electronic'},
        {'name': 'amazon echo', 'price': -49.99, 'type': 'Electronic'},
    ]
    with pytest.raises(ValueError):
        for record in records:
            price = record['price']
            if price < 0 or price == 0 or price > sys.maxsize:
                raise ValueError("Incorrect price")
    assert calculate_total('NJ', records) is None
    assert calculate_total('PA', records) is None
    assert calculate_total('DE', records) is None


def test_tax_exempt_items():
    records = [
        {'name': 'Apples', 'price': 1.99, 'type': 'Wic Eligible food'},
        {'name': 'Shirt', 'price': 19.99, 'type': 'Clothing'},
        {'name': 'Book', 'price': 9.99, 'type': 'Everything else'},
    ]
    assert calculate_total('NJ', records) == 32.63
    assert calculate_total('PA', records) == 32.57
    assert calculate_total('DE', records) == 31.97


# testing for fur vs non-fur clothes
def test_taxable_clothing_items():
    records = [
        {'name': 'Fox Fur Coat', 'price': 1984.99, 'type': 'Clothing'},
        {'name': 'Tuttle Neck Sweater', 'price': 39.99, 'type': 'Clothing'},
    ]
    assert calculate_total('NJ', records) == 2155.99
    assert calculate_total('PA', records) == 2024.98
    assert calculate_total('DE', records) == 2024.98


def test_default_tax_rate_items():
    records = [
        {'name': 'TV', 'price': 599.99, 'type': 'Everything else'},
        {'name': 'Jeans', 'price': 49.99, 'type': 'Clothing'},
        {'name': 'Bananas', 'price': 0.99, 'type': 'Wic Eligible food'},
    ]
    assert calculate_total('NJ', records) == 690.57
    assert calculate_total('PA', records) == 686.97
    assert calculate_total('DE', records) == 650.97


def test_maxint():
    records = [
        {'name': 'Blank Check', 'price': sys.maxsize+1, 'type': 'Bank Check'},
    ]
    assert calculate_total('NJ', records) is None
    assert calculate_total('PA', records) is None
    assert calculate_total('DE', records) is None
