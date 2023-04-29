# software_homework
## To run code
+ using python3.10
+ pip install -r requirements.txt
+ run in main.py

## Test the function working
+ under if __name__== '__main__':
+ change the records data to test other values.
+ print(calculate_total(<'state letters'>, records))

## Production function
### calculate_total
+ This function get state letters and records
+ By item type and state, accept different tax rate.
+ In python, float values' summation is not correct like 0.1 + 0.2 = 0.30000000000000004
  So using round function to handle this
+ After calculate all the items in record, return the total
