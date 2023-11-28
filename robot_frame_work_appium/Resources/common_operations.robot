*** Settings ***
Library       AppiumLibrary
Resource    ./Common_variables.robot
*** Keywords ***
Opening the general app application
    open application    ${Server}    devicename=${Device_name}   platformName=${Platform_name}    appPackage=${App_package}      appActivity=${App_activity}

Closing the general store application
    close application