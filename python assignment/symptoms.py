'''
Arfan Danial Bin Zainal Abidin, 20284997
Chau Lindon, 20284682

Question No.4
'''

import validation
import calculate

def getSymp():   
    Qlist=['U','H','W','V','D','I','T','S']
    anslist=[]
    error=[]
    count=0
    line='-'*59
    
    for i in range(len(Qlist)):
        getchoice(Qlist[i])
        answer=input('Yes-2  Sometimes-1  No-0: ')
        jawapan=validation.valid(answer)
        if jawapan=='valid':
            anslist.append(answer)
        else:
            anslist.append('o')
            count+=1
            
    if count>0:
        print(line)
        print('You have entered invalid data',count,'time(s)')
        print('You will have to re-enter the data')
        print(line)
        
    for x in range(len(anslist)):
        if anslist[x]=='o':
            error.append(x)

    for y in range(count):
        getchoice(Qlist[error[y]])
        new=input('Yes-2  Sometimes-1  No-0: ')
        newer=validation.valid(new)
        anslist.remove('o')
        if newer=='valid':
            anslist.insert(error[y],new)
        else:
            print(line)
            print('You failed to enter valid data!')
            print('Results cannot be computed')
            print(line)
            break
        
    if len(anslist)==8:
        calculate.risk(anslist)
    

def getchoice(option):
    if option=='U':
        print('\nQ1.Do you frequently urinate at night?')

    elif option=='H':
        print('\nQ2.Do you experince extreme hunger despite you are eating?')
    
    elif option=='W':
        print('\nQ3.Are you having unintended weight loss?')

    elif option=='V':
        print('\nQ4.Have you had any sudden blurred in vision?')
        
    elif option=='D':
        print('\nQ5.Do you feel thirsty more often than usual?')

    elif option=='I':
        print('\nQ6.Are you having more infections than usual?')

    elif option=='T':
        print('\nQ7.Do you often experince body fatigue?')

    elif option=='S':
        print('\nQ8.Are you having sores that heal significantly slow?')

        
    
    
    
    
    


                
