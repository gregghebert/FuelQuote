# FuelQuote
Software Design Project (Summer 2019)

Project:
COSC 6353 / 4353

Description: 
A partner of your company has requested to build a software application that will predict the
fuel rate based on the following criteria:
- Client Location
- Competitors rate
- Client rate history
- Gallons requested
- Company profit margin (%)
- Seasonal rate fluctuation (%)

Software must include following components:
- Login (Allow Cleint to register if not a client yet)
- Cleint Registration (Initially only username and Password)
- Client Profile Management (After client registers they should login first to complete profile)
- Fuel Quote Form with Pricing module (Once user enters all required information pricing module predicts the rate)
- Fuel Quote History


Here are the details:

1. DATABASE: Database must include following tables:
- Login
- Client Information
- Fuel Quote

Important deliverables:
- You should have validations in place for required fields, field types, and field lengths. 
- Backend should retreive data from DB and display it to front end.
- Form data should be polulated from backend. Backend should receive data from front end, validate, and persist to DB.
 
2. PRICING MODULE: Create a pricing module that should predict the price per gallon based on this formula.

Suggested Price = Current Price + Margin

Where,

Current price per gallon = $1.50 (this is the price what distributor gets from refinary and it varies based upon crude price. But we are keeping it constant for simplicity)
Margin =  Current Price * (Location Factor - Rate History Factor + Gallons Requested Factor + Company Profit Factor + Rate Fluctuation)

Consider these factors:

Location Factor = 2% for Texas, 4% for out of state.
Rate History Factor = 1% if client requested fuel before, 0% if no history (you can query fuel quote table to check if there are any rows for the client)
Gallons Requested Factor = 2% if more than 1000 Gallons, 3% if less
Company Profit Factor = 10% always
Rate Fluctuation = 4% for summer, 3% otherwise

Example:
1500 gallons requested, in state, does have history (i.e. quote history data exist in DB for this client)

Suggested Price/gallon = 1.50 + (.02 - .01 + .02 + .1 + .03) * 1.50 = $1.74

Total Amount Due = 1500 * 1.74 = $2610

Additional Validations:
•	Make suggested price and total amount fields in your Quote form read-only, i.e. user cannot enter these values.
•	Create another button on Quote Form before Submit, call it "Get Price".
•	After user enters all other fields in the form other than Suggested Price and Total Amount, allow user to click on "Get Price", i.e. Get Price and Submit Quote buttons should be disabled if there are no values entered in the form. 
•	When user clicks on "Get Price" button make a call to Pricing Module and get the suggested price. 
•	Display Suggested Price and Total Amount once you get the values from pricing module. 
•	Make sure you do not lose any form values when you make a call to Pricing modul
•	You can use AJAX call to achieve this. There are other ways. 
•	Then user clicks on Submit Quote and you save the quote.
•	We are not allowing price negotiation at this point.
