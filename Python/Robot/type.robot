*** Test Cases ***
Check Variable Types
    ${number} =     Set Variable    123
    ${text} =     Set Variable    Hello
    ${list} =     Create List    1    2    3
    ${dict} =     Create Dictionary    name = John    age = 30

    ${number_type} =     Evaluate    type(${number}).__name__
    ${text_type} =     Evaluate    type('${text}').__name__
    ${list_type} =     Evaluate    type(${list}).__name__
    ${dict_type} =     Evaluate    type(${dict}).__name__


    Log    Number type: ${number_type}
    Log    Text type: ${text_type}
    Log    List type: ${list_type}
    Log    Dict type: ${dict_type}