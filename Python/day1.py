#s=input()
#if(s.isalpha):
#    print("Yes")
# else:
#     print("No")

def logger(msg):
    def log_message():
        print('Log:', msg)
    return log_message
log_hi = logger('Hi')
log_hi()