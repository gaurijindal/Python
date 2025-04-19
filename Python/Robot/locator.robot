*** Settings ***
Documentation    To Locate a Product
Library    SeleniumLibrary
Test Setup    Open the browser with saucedemo
Test Teardown    Close Browser
Resource    resource.robot
 
*** Test Cases ***
Validate Unsuccessful login
    Fill the login Form    ${user_name}    ${valid_password}
    wait till a element is visible    xpath://*[@id="shopping_cart_container"]/a
    Verify Card Titles In The Shop Page
    Select the Card    Sauce Labs Fleece Jacket
 
 
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

Select the Card
    [Arguments]    ${card_name}
    ${elements}=        Get WebElements    css:.inventory_item_name
    ${index}=    Set Variable    1
    FOR    ${element}    IN    @{elements}
        ${text}=    Get Text    ${element}
        Exit For Loop If    '${card_name}' == '${text}'
                #${index} =    ${index} + 1
                ${index}=    Evaluate    ${index} + 1

    END
    Log    ${index}
    Click Button    xpath:(//*[@class='pricebar'])[${index}]/button