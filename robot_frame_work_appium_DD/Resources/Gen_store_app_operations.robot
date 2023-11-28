*** Settings ***
Resource    ../Resources/Gen_store_resource.robot

*** Keywords ***

Clicking country drop down
    wait until page contains element    ${General_store_locators}[county_drop_down]     15s
    click element       ${General_store_locators}[county_drop_down]


Selecting desired country from the drop down
    ${i}    Evaluate    1       #i=1
    WHILE    ${i}>0
        ${LIST_ELEMENTS}    get webelements    ${General_store_locators}[country_items]
        FOR    ${elem}      IN      @{LIST_ELEMENTS}
            ${country}      get element attribute    ${elem}    text
            IF      "${country}" == ${General_store_locators}[country_name]
                click element    ${elem}
                ${i}   evaluate    ${i}-1
                BREAK
            END
        END
        Swipe    789    2088    178    595    500
        sleep    3s
    END

Entering name
    input text       ${General_store_locators}[name_filed]     ${General_store_locators}[name_field_data]

Clicking gender radio button
    click element    ${General_store_locators}[male_radio_button]

Click on proceed to shop button
    click element    ${General_store_locators}[lets_shop_button]
    wait until page contains    Products

Selecting a shoe from the shoes item page & adding to cart
   ${i}    Evaluate    1
    WHILE    ${i}>0
        ${LIST_ELEMENTS}    get webelements    ${General_store_locators}[shoe_items_list]
        FOR    ${elem}      IN      @{LIST_ELEMENTS}
            ${shoe}      get element attribute    ${elem}    text
            IF      "${shoe}" == ${General_store_locators}[Shoe_name]
                click element       ${General_store_locators}[add_to_cart_shoe]
                ${i}   evaluate    ${i}-1
                BREAK
            END
        END
        Swipe     1052    1063    28    256   500
         sleep     4s
    END

Click on cart button
    click element    ${General_store_locators}[cart_button]

Click on the email subscribe check box
    sleep    3s
    click element    ${General_store_locators}[email_subscribe_check_box]

Click on proceed to payment button
    click element    ${General_store_locators}[payment_proceed]

Click on terms & conditions field
    long press      ${General_store_locators}[terms_conditions]
    sleep    3s
    click element    ${General_store_locators}[close_terms_conditions]