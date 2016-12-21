usernames=['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

usernames_input = str(input("Enter your username"))

while usernames_input not in usernames:
    print("Access Denied")
    usernames_input = str(input("Enter your username"))
print("Access Granted")

