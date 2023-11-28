*** Settings ***
Library       AppiumLibrary
Resource      ../Data_setup/data_fetch.robot

*** Keywords ***
Opening the general app application
    common locators read from excel file
    general store locators read from excel file
    open application    ${common_locators}[server]    devicename=${common_locators}[Device_name]   platformName=${common_locators}[Platform_name]    appPackage=${common_locators}[App_package]      appActivity=${common_locators}[App_activity]

Closing the general store application
    close all applications