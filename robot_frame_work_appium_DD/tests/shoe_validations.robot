*** Settings ***
Resource   ../Resources/Gen_store_resource.robot
Test Setup    Opening the general app application
Test Teardown    Closing the general store application

*** Test Cases ***
Adding a shoe to the cart & proceed to checkout page
    Clicking country drop down
    Selecting desired country from the drop down
    Entering name
    Clicking gender radio button
    Click on proceed to shop button
    Selecting a shoe from the shoes item page & adding to cart
    Click on cart button
    Click on the email subscribe check box
    Click on proceed to payment button


Adding a shoe to the cart & checking terms & conditions
    Clicking country drop down
    Selecting desired country from the drop down
    Entering name
    Clicking gender radio button
    Click on proceed to shop button
    Selecting a shoe from the shoes item page & adding to cart
    Click on cart button
    Click on the email subscribe check box
    Click on terms & conditions field