*** Settings ***
Documentation    To Verify the item in the cart
Library    SeleniumLibrary
Test Setup    Open the browser with saucedemo
Test Teardown    Close Browser
Resource    resource.robot
 
*** Test Cases ***
Validate Unsuccessful login
    Fill the login Form    ${user_name}    ${valid_password}
    wait till a element is visible    xpath://*[@id="shopping_cart_container"]/a
    Verify Card Titles In The Shop Page
   
 
 
*** Keywords ***
 
Fill the loginForm
    [Arguments]    ${username}    ${password}
    Input Text    user-name    ${user_name}
    Input Password    password    ${password}
    Click Button    login-button
 
wait till a element is visible
    [Arguments]    ${element}
    Wait Until Element Is Visible    ${element}
 
Verify Card Titles In The Shop Page
    ${expectedlist}=    Create List
    ...    Sauce Labs Backpack
    ...    Sauce Labs Bolt T-shirt
    ...    Sauce Labs Bike Light
    ...    Sauce Labs Fleece Jacket
    ...    sauce Labs Onesie
    ...    Test.allTheThings() T-shirt (Red)
    ${elements}=    Get WebElements    css:inventory_item_name
    FOR    ${element}    IN    @{elements}
        ${test}=    Get Text    ${element}
        Should Contain    ${expectedlist}    ${test}
        Log    Validated Card Title: ${test}
       
    END