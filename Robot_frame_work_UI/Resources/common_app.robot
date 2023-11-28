*** Settings ***
Library    SeleniumLibrary

*** Keywords ***

begin web test
    Set Selenium Speed    .2s
	Set Selenium Timeout    7s
	Open Browser       ${URL}     ${browser}
	Maximize Browser Window

close web test
	Close Browser