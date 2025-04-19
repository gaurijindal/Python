*** Test Cases ***
Create And Log A List
    @{my_list} =    Create List     Apple    Banana    Mango
    Log    ${my_list}

Loop Through List
    @{fruits} =    Create List     Apple     Banana     Mango
    FOR    ${fruit}    IN    @{fruits}
        Log    I like ${fruit}
        
    END
    
Check if Mango Is In The List
    @{fruits} =     Create List    Apple     Banana     Mango
    ${is_mango_present} =     Evaluate     'Mango' in ${fruits}
    Run Keyword If    ${is_mango_present}    Log    Mango is in

Find a Specific Fruit
    @{fruits} =     Create List    Apple     Banana     Mango
    FOR    ${fruit}    IN    @{fruits}
        Run Keyword If    '${fruit}' == 'Banana'     Log    Found Banana!
        
    END

Count Items in List
    @{fruits} =     Create List    Apple     Banana     Mango
    ${count} =     Get Length    ${fruits}
    Log     There are ${count} fruits in the list.
    
    