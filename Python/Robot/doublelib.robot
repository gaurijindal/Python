*** Settings ***
# Library    BuiltIn 
Library    Collections

*** Test Cases ***
Add And Remove Items In List
    @{fruits} =     Create List    Apple     Banana
    Log    Original list: ${fruits}

    #Add Items
    Append To List    ${fruits}    Mango
    Append To List    ${fruits}    Grapes
    Log    After adding: ${fruits}

    #Removing Item
    Remove From List    ${fruits}    1
    Log    After removing index 1 (Banana): ${fruits}

Check Fruit Availability
    ${my_fruit} =     Set Variable    Banana
    @{fruits} =     Create List    Apple    Banana    Mango

    Run Keyword If    '${my_fruit}' in ${fruits}    Log    ${my_fruit} is available
    # Run Keyword Unless     '${my_fruit}' in ${fruits}    Log    ${my_fruit} is NOT available

Filter List Items Starting with A
    @{fruits} =     Create List    Apple    Banana    Apricot    Mango
    @{filtered} =    Create List

    FOR    ${fruit}    IN    @{fruits}
        Run Keyword If    '${fruit}'[0] == 'A'    Append To List    ${filtered}    ${fruit}
    END
    
Count Elements Without Get Length
    @{mylist} =    Create List    Apple    Banana    Mango    Orange

    ${count} =    Set Variable    0
    FOR    ${item}    IN    @{mylist}
        ${count} =     Evaluate    ${count} + 1
    END

    Log    Total elemets in list: ${count}
