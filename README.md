# Soko
Soko is a basic e-commerce platform built on django framework where individuals can buy/sell different products. To purchase a product, the buyer contacts the seller directly. The inbox feature facilitates communication between the buyer and seller. 
Products are grouped by categories.
## Features
- Browse and purchase items as a buyer
- Add items to sell as a seller
- Dashboard to view items put up for sale
- Chat/Inbox

## Test

To test the application locally, clone the repo and run the following:

`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

The application is accessible at http://127.0.0.1:8000/

## Todo
1. [x] Sign/Log Out
2. [] Password Reset
3. [] Add Cart
