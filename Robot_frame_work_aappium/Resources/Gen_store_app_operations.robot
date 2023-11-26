*** Settings ***
Resource    ./gen_resource.robot

*** Keywords ***
Clicking country drop down
    wait until page contains element    ${county_drop_down}     15s
    click element       ${county_drop_down}

Selecting desired country from the drop down
    sleep    5s
    ${i}    Evaluate    1
    WHILE    ${i}>0
        ${LIST_ELEMENTS}    get webelements    ${country_items}
        ${LIST_LENGTH}    get length        ${LIST_ELEMENTS}
      FOR    ${elem}      IN      @{LIST_ELEMENTS}
        ${country}      get element attribute    ${elem}    text
        IF      "${country}" == ${country_name}
            click element    ${elem}
            ${i}   evaluate    ${i}-1
            BREAK
        END
      END
      Swipe    789    2088    178    595    500
    END

Entering name
    input text       ${name_filed}     ${name_field_data}

Clicking gender radio button
    click element    ${male_radio_button}

Click on proceed to shop button
    click element    ${lets_shop_button}
    wait until page contains    Products

Selecting a shoe from the shoes item page & adding to cart
   ${i}    Evaluate    1
    WHILE    ${i}>0
      ${LIST_ELEMENTS}    get webelements    ${shoe_items_list}
      FOR    ${elem}      IN      @{LIST_ELEMENTS}
        ${shoe}      get element attribute    ${elem}    text
        IF      "${shoe}" == ${Shoe_name}
            click element       ${add_to_cart_shoe}
            ${i}   evaluate    ${i}-1
            BREAK
        END
      END
      Swipe     1052    1063    28    256   500
    END

Click on cart button
    click element    ${cart_button}

Click on the email subscribe check box
    sleep    5s
    click element    ${email_subscribe_check_box}

Click on proceed to payment button
    click element    ${payment_proceed}

Click on terms & conditions field
    long press      ${terms_conditions}
    sleep    3s
    click element    ${close_terms_conditions}