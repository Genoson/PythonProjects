"""
QAP 3 copilot test
Stephen Squire
November 2, 2021
I used copilot to attempt solve this QAP assignment in as little time as possible, 
with as little effort from myself, the coder, as possible. 
This took me about 30 minutes to complete.
The last test run I did, the one stop insurance company, while very similar to this problem 
in complexity took me ~ 1.5 hours. That was my first real use of copilot. This attempt
came after a few weeks of practice and learning its idiosyncrosies and its limitations.
Getting my coding time down by a further factor of 3 after already more than halfing the
amount of time i would have spent on this assignment was a huge accomplishment.
Copilot is a great tool for solving problems, but it is to be used cautiously as it
can be very difficult to get the right answer if you don't know what the right answer
should look like.
Further corrections to the code copilot provided are still required in order to make it
perfectly in line with the desired outputs of the QAP.
"""

"""
QAP 3 – Loops, Strings and Dates
Honest Harry owns a used car lot and would like a program to keep track of his sales. Follow good programming practise using Comments, Constants, and Spacing.
The program will repeat until the user enters the word “END” for the Customer First Name or a prompt at the end of the program asking the user if they want to enter another sale.
For each car sold, the user is required to enter the customer first name and last name (must be entered – adjust to title case), the phone number (must be entered - must be 10 digits) , the purchase date (must be entered and in the format YYYY-MM-DD), the plate number (must be entered – must be 6 characters - convert to all caps – BONUS: entered in the format XXX999), the car make, the year, the selling price (does not exceed $50,000.00), the amount of the trade in (does not exceed the selling price), the salespersons name, and finally a credit card number and expiry date. NOTE: Only fields with formats specified need to be validated – you can do them all if you want.
The program should calculate the price after trade, the taxes, the licence fee, the transfer fee, and the total sales price. The price after trade is the selling price less the trade in amount. Taxes (HST) are calculated at 15% on the selling price. The licence fee is standard rate in NL of $75.00 on cars up to and including $5,000.00 and $165.00 on cars over $5,000.00. The transfer fee 1% of the selling price - if the selling price is more than $20,000.00, an additional 1.6% luxury tax is calculated on the selling price and added to the licence fee. The total sales price is the price after trade plus taxes plus the licence fee and the transfer fee.
Display the following payment schedule to the screen based on the number of years the customer will use to pay off the car. For each of 4 years, calculate the number of payment (monthly), the total price as the total sales price plus a financing fee of $39.99 per year. Divide this number by the number of months to get the monthly payment. Finally, display the purchase date (use the current date) and the first payment date – 30 days after the purchase date.
1234567 1234567890123456789012345678901234567890123456789012345678901234567890 # Years # Payments Financing Fee Total Price Monthly Payment ----------------------------------------------------------------------
1 12
2 24
3 36
4 48
 $39.99       $12,838.00
 $78.98       $12,916.98
$119.97       $12,957.97
$159.96       $12,997.96
$1,069.83
  $538.22
  $359.94
  $270.79
At this point, allow the user to enter the payment method they wish to use – they will enter the number of years based on the chart shown – must be between 1 and 4. Put a blank line before and after the input.
Enter the payment schedule you want to follow (1-4): #
Display the remaining output to the screen based on the following guidelines. The Invoice date is the purchase date. Customer name is the first initial and the last name. Car Details are the Year, Make and
Model – ie: 2014 Toyota Corolla. The terms are the payment method entered (1-4) and the total payments is the payment method (this is the number of years) * 12 to get the total months. Finally, the monthly payment is the same calculation as defined previously.
The program should create a Receipt ID for the sale in the form XX-XXX-XXXX where the first two characters are the customer initials, the middle 3 characters are the last 3 digits in the license plate number, and the final 4 characters are the last 4 digits of the phone number.
1234 1234567890123456789012345678901234567890
       Honest Harry Car Sales
      Used Car Sale and Receipt
Invoice Date: Mon dd, yyyy
Receipt No: XX-XXX-XXXX
Sold to:
     X. XXXXXXXXXXXXXXXXXXXXXXXXXX
     XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
     XXXXXXXXXXXXXXXXXXX,XX,XXXXXX
Car Details:
     XXXX XXXXXXXXXXXXX XXXXXXXXXX
Sale price:
Trade Allowance:
Price after Trade:
HST:
License Fee:
Transfer Fee:
Total Sales Cost:
$99,999.99
$99,999.99
$99,999.99
----------
$99,999.99
$99,999.99
$99,999.99
----------
$99,999.99
Terms: 9        Total payments: 99
Monthly payment:         $9,999.99
    Honest Harry Car Sales
Best used cars at the best price!

"""

# Imports
import datetime
import re

# Constants

HST_RATE = 0.15
LICENCE_FEE_RATE_1 = 75
LICENCE_FEE_RATE_2 = 165
LICENCE_FEE_THRESHOLD = 5000
LUXURY_TAX_RATE = 0.016
LUXURY_TAX_THRESHOLD = 20000
TRANSFER_FEE_RATE = .01
FINANCING_FEE_RATE = 39.99
MAX_SALE_PRICE = 50000
MAX_TRADE_ALLOWANCE = 50000

# start of main program

while True:
    # inputs with validations for each
    while True:
        customer_first_name = input("Enter customer first name: ").title()
        if customer_first_name.isalpha():
            break
        else:
            print("Invalid input, please enter a valid first name")
    
    while True:
        customer_last_name = input("Enter customer last name: ").title()
        if customer_last_name.isalpha():
            break
        else:
            print("Invalid input, please enter a valid last name")
    
    while True:
        customer_phone_number = input("Enter customer phone number: ")
        if re.match(r'^\d{10}$', customer_phone_number):
            break
        else:
            print("Invalid input, please enter a valid phone number")
    
    while True:
        try:
            purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
            purchase_date = datetime.datetime.strptime(purchase_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid input, please enter a valid date")
    
    while True:
        plate_number = input("Enter plate number: ").upper()
        if re.match(r'^[A-Z]{3}\d{3}$', plate_number):
            break
        else:
            print("Invalid input, please enter a valid plate number")
    
    while True:
        car_make = input("Enter car make: ")
        if car_make.isalpha():
            break
        else:
            print("Invalid input, please enter a valid car make")
    
    while True:
        car_model = input("Enter car model: ")
        if car_model.isalpha():
            break
        else:
            print("Invalid input, please enter a valid car model")
    
    while True:
        try:
            car_year = int(input("Enter car year: "))
            if car_year > 1900 and car_year < datetime.datetime.now().year:
                break
            else:
                print("Invalid input, please enter a valid car year")
        except ValueError:
            print("Invalid input, please enter a valid car year")
    
    while True:
        try:
            car_price = float(input("Enter car price: "))
            if car_price > 0 and car_price <= MAX_SALE_PRICE:
                break
            else:
                print("Invalid input, please enter a valid car price")
        except ValueError:
            print("Invalid input, please enter a valid car price")
    
    while True:
        try:
            trade_allowance = float(input("Enter trade allowance: "))
            if trade_allowance >= 0 and trade_allowance <= car_price:
                break
            else:
                print("Invalid input, please enter a valid trade allowance")
        except ValueError:
            print("Invalid input, please enter a valid trade allowance")
    
    while True:
        sales_person = input("Enter sales person: ")
        if sales_person.isalpha():
            break
        else:
            print("Invalid input, please enter a valid sales person")
    
    while True:
        credit_number = input("Enter credit card number: ")
        if re.match(r'^\d{16}$', credit_number):
            break
        else:
            print("Invalid input, please enter a valid credit card number")
    
    while True:
        try:
            credit_expiry = input("Enter credit card expiry date (YYYY-MM): ")
            credit_expiry = datetime.datetime.strptime(credit_expiry, "%Y-%m")
            break
        except ValueError:
            print("Invalid input, please enter a valid credit card expiry date")
    
    # calculations
    customer_initials = customer_first_name[0] + customer_last_name[0]
    customer_phone_number_last_4 = customer_phone_number[-4:]
    customer_license_plate_number_last_3 = plate_number[-3:]
    receipt_id = customer_initials + "-" + customer_license_plate_number_last_3 + "-" + customer_phone_number_last_4

    price_after_trade = car_price - trade_allowance
    hst = price_after_trade * HST_RATE
    if car_price < LICENCE_FEE_THRESHOLD:
        licence_fee = LICENCE_FEE_RATE_1
    else:
        licence_fee = LICENCE_FEE_RATE_2
    
    if car_price < LUXURY_TAX_THRESHOLD:
        transfer_fee = TRANSFER_FEE_RATE * car_price
    else:
        transfer_fee = (TRANSFER_FEE_RATE + LUXURY_TAX_RATE) * car_price

    total_sales_cost = car_price + hst + licence_fee + transfer_fee

    # financing over 4 years output using the below formatting printed as a table using a while loop for the interior
    """
    1234567 1234567890123456789012345678901234567890123456789012345678901234567890 
    # Years # Payments Financing Fee Total Price Monthly Payment 
    # ----------------------------------------------------------------------
    1 12  $39.99       $12,838.00 $1,069.83
    2 24 $78.98       $12,916.98 $538.22
    3 36 $119.97       $12,957.97 $359.94
    4 48 $159.96       $12,997.96 $270.79"""

    print("{:^6}{:^12}{:^16}{:^12}{:^20}".format( "Years", "Payments", "Financing Fee", "Total Price", "Monthly Payment"))
    print("{}{}{}{}{}".format( "-", "-", "-", "-", "-" * 40))
    for i in range(1, 5):
        print("{:^6}{:^12}{:^16}{:^12}{:^20}".format(i, i * 12, "$" + str(round(FINANCING_FEE_RATE * i, 2)), "$" + str(round(total_sales_cost, 2)), "$" + str(round(total_sales_cost / (i * 12), 2))))
    print("{}{}{}{}{}".format( "-", "-", "-", "-", "-" * 40))

    # ask user terms of purchase, 1 -4
    while True:
        terms = input("Enter terms of purchase: ")
        if terms.isdigit():
            terms = int(terms)
            if terms > 0 and terms < 5:
                break
            else:
                print("Invalid input, please enter a valid terms of purchase")
        else:
            print("Invalid input, please enter a valid terms of purchase")

    # receipt generation using the below formatting, 40 characters wide with space between
    """
           Honest Harry Car Sales
      Used Car Sale and Receipt
    Invoice Date: Mon dd, yyyy
    Receipt No: XX-XXX-XXXX
    Sold to:
        X. XXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXX,XX,XXXXXX
    Car Details:
        XXXX XXXXXXXXXXXXX XXXXXXXXXX
    Sale price: $99,999.99
    Trade Allowance: $99,999.99
    Price after Trade: $99,999.99
                                ----------------
    HST: $99,999.99
    License Fee: $99,999.99
    Transfer Fee: $99,999.99
                                ----------------
    Total Sales Cost: $99,999.99

    Terms: 9        Total payments: 99
    Monthly payment:         $9,999.99
        Honest Harry Car Sales
    Best used cars at the best price!
        """
    
    print("{:^40}".format("Honest Harry Car Sales"))
    print("{:^40}".format("Used Car Sale and Receipt"))
    print("{:^40}".format("Invoice Date: " + str(datetime.datetime.now().strftime("%a %d, %Y"))))
    print("{:^40}".format("Receipt No: " + receipt_id))
    print("{:^40}".format("Sold to:"))
    print("{:^40}".format("    " + customer_first_name + " " + customer_last_name))
    #print("{:^40}".format("    " + customer_address))
    #print("{:^40}".format("    " + customer_city + ", " + customer_province + " " + customer_postal_code))
    print("{:^40}".format("Car Details:"))
    print("{:^40}".format("    " + car_make + " " + car_model + " " + car_year))
    print("{:^40}".format("Sale price: $" + str(car_price)))
    print("{:^40}".format("Trade Allowance: $" + str(trade_allowance)))
    print("{:^40}".format("Price after Trade: $" + str(price_after_trade)))
    print("{:^40}".format("                                ----------------"))
    print("{:^40}".format("HST: $" + str(hst)))
    print("{:^40}".format("License Fee: $" + str(licence_fee)))
    print("{:^40}".format("Transfer Fee: $" + str(transfer_fee)))
    print("{:^40}".format("                                ----------------"))
    print("{:^40}".format("Total Sales Cost: $" + str(total_sales_cost)))
    print("{:^40}".format("Terms: " + str(terms) + "        Total payments: " + str(terms * 12)))
    print("{:^40}".format("Monthly payment:         $" + str(round(total_sales_cost / (terms * 12), 2))))
    print("{:^40}".format("        Honest Harry Car Sales"))
    print("{:^40}".format("Best used cars at the best price!"))

    # ask user if they want to continue
    while True:
        continue_sale = input("Continue? (y/n): ")
        if continue_sale.lower() == "y":
            break
        elif continue_sale.lower() == "n":
            print("Thank you for your business!")
            break
        else:
            print("Invalid input, please enter y or n")
    if continue_sale.lower() == "n":
        break
    else:
        continue    
