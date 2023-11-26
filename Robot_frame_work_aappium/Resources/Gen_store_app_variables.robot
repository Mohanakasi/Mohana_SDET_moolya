*** Variables ***
${county_drop_down}         android:id/text1
${country_items}            xpath=//android.widget.TextView
${country_name}             "India"
${name_filed}               id=com.androidsample.generalstore:id/nameField
${name_field_data}          Mohana kasi
${male_radio_button}        id=com.androidsample.generalstore:id/radioMale
${female_radio_button}      id=com.androidsample.generalstore:id/radioFemale
${lets_shop_button}         id=com.androidsample.generalstore:id/btnLetsShop
${Shoe_name}                "Converse All Star"
${add_to_cart_shoe}         xpath=//android.widget.TextView[@text='Converse All Star']/..//android.widget.TextView[@text='ADD TO CART']
${shoe_items_list}          xpath=//android.widget.TextView
${cart_button}              id=com.androidsample.generalstore:id/appbar_btn_cart
${email_subscribe_check_box}    xpath=//android.widget.CheckBox[@text='Send me e-mails on discounts related to selected products in future']
${payment_proceed}          id=com.androidsample.generalstore:id/btnProceed
${terms_conditions}         id=com.androidsample.generalstore:id/termsButton
${close_terms_conditions}   id=android:id/button1