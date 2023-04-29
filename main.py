import sys


def calculate_total(state: str, records: list) -> float:
    """
    DE: no sales tax 
    NJ: Sales tax rate is 6.6% 
    PA: Sales tax rate is 6% (we'll ignore the local tax) 
    WIC Eligible food is tax exempt in all three states 
    Clothing is exempt from in PA, and NJ except Fur clothing is taxable normally in NJ,
    we'll call it taxable if the string fur appears in a clothing item name Everything 
    else is covered under the default tax rates
    """
    # tax rates
    tax_rates = {'NJ': 1.066, 'PA': 1.06, 'DE': 0}
    # tax exemptions
    tax_exempt = ['Wic Eligible food', 'Clothing']
    # tax exemption clothing types in NJ
    taxable_clothing = {'Fur'}
    total = 0

    # Calculate subtotal
    for record in records:
        item_type = record['type']
        price = record['price']

        try:
            if price < 0 or price == 0 or price > sys.maxsize:
                raise ValueError("Incorrect price")
        except ValueError:
            return None

        match state:
            case 'DE':
                total = round(total + price, 2)
            case 'PA':
                if item_type in tax_exempt:
                    total = round(total + price, 2)
                else:
                    total = round(total + price * tax_rates[state], 2)
            case 'NJ':
                if item_type in tax_exempt:
                    if item_type == 'Wic Eligible food':
                        total = round(total + price, 2)
                    elif item_type == 'Clothing' and any(taxable in record['name'] for taxable in taxable_clothing):
                        total = round(total + price * tax_rates[state], 2)
                    else:
                        total = round(total + price, 2)
                else:
                    total = round(total + price * tax_rates[state], 2)
   
    return total


if __name__ == '__main__':
    records = [
        {'name': 'Apples', 'price': 1.99, 'type': 'Wic Eligible food'},
        {'name': 'Book', 'price': 9.99, 'type': 'Everything else'},
        {'name': 'Fox Fur Coat', 'price': 684.99, 'type': 'Clothing'},
        {'name': 'Tuttle Neck Sweater', 'price': 39.99, 'type': 'Clothing'},
        {'name': 'laptop', 'price': 1299.99, 'type': 'Electronic'},
    ]

    print(calculate_total('NJ', records))
    print(calculate_total('PA', records))
    print(calculate_total('DE', records))
