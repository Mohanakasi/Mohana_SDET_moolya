*** Settings ***
Resource    ../Resources/PO/login_page.robot
Resource    ../Resources/PO/new_customer_addition.robot

*** Keywords ***
login_validation
	login_page.click on sign in link
	login_page.Enter email id
	login_page.Enter password
	login_page.Enter password
	click on submit button

checking new customer button
	login_page.click on new customer button

Filling new customer details
	new_customer_addition.Enter email id
    new_customer_addition.Enter first name
    new_customer_addition.Enter last name
    new_customer_addition.Enter city
    new_customer_addition.Enter state
    new_customer_addition.Select gender radio button
    new_customer_addition.check the promos check box
    new_customer_addition.click on subit button

