*** Settings ***
Documentation    To Validate a login form
Library    SeleniumLibrary
#Test Teardown    Close Browser



*** Test Cases ***
Validate Successful Login
    Open the browser with saucedemo
    Fill the login Form
    # Wait Until it checks and validates user
    # Verified user loggedin


*** Keywords ***
Open the browser with saucedemo
    Open Browser    https://www.saucedemo.com/    chrome    

Fill the login form
    Input Text        id:user-name     standard_user
    Input Password    password     secret_sauce
    Click Button    login-button

# Wait Until it checks and validates user
#     Wait Until Element Is Visible    xpath://*[@id="login_button_container"]/div/form/div[3]/h3

# Verified user loggedin
#     ${result}    Get Text    xpath://*[@id="login_button_container"]/div/form/div[3]/h3
#     Should Be Equal As Strings    ${result}    Epic sadface: Username and password do not match any user in this service