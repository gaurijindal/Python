*** Settings ***
Library     SSHLibrary
Library    Telnet

*** Variables ***
${HOST}    test.rebex.net
${USERNAME}    demo
${PASSWORD}    password

*** Test Cases ***
Connect And Run Command
    Open Connection    ${HOST}
    Login    ${USERNAME}    ${PASSWORD}
    ${output} =     Execute Command    ls
    Log    ${output}
    Close Connection 