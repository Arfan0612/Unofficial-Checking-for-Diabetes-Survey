'''
Arfan Danial Bin Zainal Abidin, 20284997
Chau Lindon, 20284682

Question No.4
'''

def valid(answer): 
    if answer.isdigit():
        if len(answer)==1:
            if int(answer)>=0 and int(answer)<=2:
                return 'valid'
            else:
                errorMsg('largenumber')
        else:
            errorMsg('xsdigit')
    elif answer.isalpha():
        errorMsg('alpha')
    else:
        errorMsg('invalid')


def errorMsg(mistake):
    
    if 'alpha' in mistake:
        print('Error! characters was entered in the questionnaire')
    elif 'xsdigit' in mistake:
        print('Error! more than 1 digit is entered in the questionnaire')
    elif 'largenumber' in mistake:
        print('Error! a digit smaller than 0 or larger than 2 was entered')
    elif 'invalid' in mistake:
        print('Error! invalid data was entered')
                 
                


    

    
    


    


    
        



        

    
            
                
    
    


