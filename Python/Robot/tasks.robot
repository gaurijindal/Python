*** Settings ***
Library    Collections
*** Test Cases ***
Create a Dictionary and Log It
    @{my_dict} =     Create Dictionary    name = Gauri    age = 23    gender = Female
    Log    ${my_dict}

Add and Remove items from the Dictionary
    ${my_dict} =     Create Dictionary    name = Gauri    age = 23    gender = Female

    #Add Items
    Set To Dictionary    ${my_dict}    place = haridwar
    Log    ${my_dict}

    #Remove Items
    Remove From Dictionary    ${my_dict}    2
    Log Dictionary    ${my_dict}
