# FreshMart Grocery Billing System

This is my python project for grocery store billing. In this project, a customer buys grocery items, adds items in a loop, applies a discount coupon if they have one, and gets a receipt with 5% gst. I made this using basic python concepts like if else, while loop, functions, lists and dictionaries.

## How to Set Up and Run

Here are the step by step instructions to run this project on your system.

### Environment Setup
You only need python 3 installed. You can check if python is working by opening terminal and typing:
```bash
python --version
```

If you want to use a virtual environment (optional):
```bash
python -m venv venv
```
And activate it:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

### Dependency Instalation
This project does not use any third party modules, only standard python is used. You can run this if needed:
```bash
pip install -r requirements.txt
```

### Configuration
No database or extra setup is required. The grocery items are stored inside a python dictionary so everything runs in memory when you start the code.

### Execution

step 1 : run the main.py
Open terminal inside the project folder and type:
```bash
python main/main.py
```
(or `python src/main.py` if you are in src folder)

step 2 : enter your choice
When the program starts, you will see 4 choices. Type a number and press Enter:
- Choice 1: Shows all grocery items with code, name, category, price, stock, and available coupons.
- Choice 2: Lets you order multiple grocery items in a loop, checks stock, applies coupon discounts, and prints the bill.
- Choice 3: Shows the receipt of the last bill again if you want to check it.
- Choice 4: Exits the program.
