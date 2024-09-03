*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}    Chrome
${url}    https://www.facebook.com/

*** Test Cases ***
Testing Login Page
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    title Should Be    Facebook – log in or sign up

    Input Text    id:email    abhay@pintunubhai.com
    Input Text    id:pass    dalchawalnobhaja
    #Click Element    xpath://button[@class='_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy']
    Click Link    xpath://a[@class="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy"]
    Sleep    5
    Input Text    xpath:(//input[@class="inputtext _58mg _5dba _2ph-"])[1]    Abhaya kumar
    Input Text    xpath:(//input[@name="lastname"])    Paikaraya
    Input Text    xpath:(//input[@class="inputtext _58mg _5dba _2ph-"])[3]    8397053491
    Input Text    xpath://input[@id="password_step_input"]    dalchawal123
    #Handle Dropdown
    Select From List By Label    id:day    15
    Select From List By Label    id:day    25
    Select From List By Label    id:month    Feb
    Select From List By Index    id:year    5
    #Handle Radio button
    Select Radio Button    sex    2
    #

    
*** Keywords ***
