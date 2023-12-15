*** Settings ***
Library    DataDriver      file=C:\SDET\Python\temp1.csv    dialect=Excel-EU
Library    SeleniumLibrary
Test Template    Login With User And Password


*** Test Cases ***
this is sample test case ${a} ${b}




*** Keywords ***
Login With User And Password
    [Arguments]    ${a}     ${b}
    log to console    ${a}
    log to console    ${b}

