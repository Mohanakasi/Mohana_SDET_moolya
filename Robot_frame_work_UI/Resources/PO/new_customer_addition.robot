*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Enter email id
    Input Text    id=EmailAddress      kasi.jmr@gmail.com
Enter first name
    Input Text    id=FirstName  Mohana Kasi
Enter last name
    Input Text    id=LastName   Settipalli
Enter city
    Input Text    id=City       Guntur
Enter state
    Select From List By Value    id=StateOrRegion   AL
Select gender radio button
    Select Radio Button         gender          male
check the promos check box
    Select Checkbox    name=promos-name
click on subit button
    sleep    6s
    Click Button    xpath=//button[text()='Submit']