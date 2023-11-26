*** Settings ***
Resource    ../Resources/Gen_store_resource.robot

*** Keywords ***
Opening the general app application
    open application    ${Server}    devicename=${Device_name}   platformName=${Platform_name}    appPackage=${App_package}      appActivity=${App_activity}