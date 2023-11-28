*** Settings ***
Library    openpyexcel
Library    excel
Library       ../Data_setup/locators_read_excel.py

*** Variables ***

*** Keywords ***
common locators read from excel file
    ${common_locators}       locators_read_excel.Excel data read    ..\\robot_frame_work_aappium_DD\\Data_setup\\test_data_fk.xlsx       common locators      A    B
    set global variable   ${common_locators}
    [Return]            ${common_locators}

general store locators read from excel file
    ${General_store_locators}       locators_read_excel.Excel data read    ..\\robot_frame_work_aappium_DD\\Data_setup\\test_data_fk.xlsx    general store      A    B
    set global variable   ${General_store_locators}
    [Return]            ${General_store_locators}