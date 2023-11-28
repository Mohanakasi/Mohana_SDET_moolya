*** Settings ***
Documentation       Trial suitr
Library             SeleniumLibrary
Resource            ../Resources/crm_app.robot
Resource            ../Resources/common_app.robot
Suite Setup         common_app.begin web test
Suite Teardown      common_app.close web test

*** Variables ***
${BROWSER} =    chrome
${URL} =   https://automationplayground.com/crm
${LOGIN_SEARCH_TERM} =  Our Happy Customers

*** Test Cases ***
Should able to click sign in link and navigate to login page
	[Documentation]    sign-link
	[Tags]             Sign-in
    crm_app.login_validation

Should able to click on new customer link
	[Documentation]    new_cutomer button validation
	[Tags]             new_customer
    crm_app.checking new customer button

Should able add the data of new customer
	[Documentation]     adding new customer
	[Tags]              new_customer_data
	crm_app.Filling new customer details


*** Keywords ***
