*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
click on sign in link
#	Click Link        xpath=//a[@id='SignIn']
    Click Link        SignIn
    Page Should Contain    Login
Enter email id
    Input Text    id=email-id   kasi.jmr@gmail.com
Enter password
    Input Password    id=password   12345
click on submit button
    capture page screenshot
    Click Button    id=submit-id
    Page Should Contain    ${LOGIN_SEARCH_TERM}


click on new customer button
	Click Link    id=new-customer