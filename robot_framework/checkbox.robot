*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}    Chrome
${url}    https://www.functionize.com/free-trial
    
*** Test Cases ***
Select CheckBoxes
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Title Should Be    Functionize: Get Free Trial
    Select Checkbox    i_m_interested_in_learning_more_about0-46e27199-313a-4a78-bd72-b85b29dd0158
    Select Checkbox    i_m_interested_in_learning_more_about1-46e27199-313a-4a78-bd72-b85b29dd0158
    Select Checkbox    i_m_interested_in_learning_more_about2-46e27199-313a-4a78-bd72-b85b29dd0158
    Select Checkbox    i_m_interested_in_learning_more_about3-46e27199-313a-4a78-bd72-b85b29dd0158
    
*** Keywords ***
