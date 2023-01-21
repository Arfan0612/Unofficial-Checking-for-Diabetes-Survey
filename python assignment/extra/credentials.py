def getNameID():
    names=input('\nEnter your name: ')
    studentid=input('enter your student ID: ')
    validation(names.split(),studentid)
    
def validation(names,studentid):
    namevalid=False
    idvalid=False
    
    for r in names:
        if r.isalpha():
            firstname=names[0]
            namevalid=True
        else:
            namevalid=False

    if studentid.isdigit():
        if len(studentid)==8:
            idvalid=True
    furthervalid(firstname,studentid,namevalid,idvalid)

def furthervalid(firstname,studentid,namevalid,idvalid):
    if namevalid and idvalid:
        printMsg(firstname,studentid)
        
    elif namevalid and not(idvalid):
        print('\nerror, enter 8-digit numbers')
        retry()
        
    elif idvalid and not(namevalid):
        print('\nerror, enter your name in characters')
        retry()
        
    else:
        print('\nerror, enter 8-digit numbers')
        print('error, enter your name in characters')
        retry()
            
def retry():
    retry=input('Do you want to enter credentials again? Y-yes other keys-no: ')
    if retry.upper()!='Y':
        print('\nResults cannot be computed')
        print('Have a nice day!')   
    else:
        getNameID()

def printMsg(firstname,studentid):
    print('\nHi, '+firstname.title()+' and your student ID is',studentid)
    print('You may proceed with the questioning')
     
            
getNameID()
