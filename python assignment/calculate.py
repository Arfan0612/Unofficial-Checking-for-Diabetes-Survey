'''
Arfan Danial Bin Zainal Abidin, 20284997
Chau Lindon, 20284682

Question No.4
'''

def risk(anslist):
    attempt=1
    total=0
    while attempt<=len(anslist):
        add=int(anslist[attempt-1])
        total+=add
        attempt+=1

    if total<=5:
        result('Low')
    elif total>=14:
        result('High')
    else:
        result('Moderate')

def result(danger):
    print('\n-----------------------------------------------------')
    print('Risk Level for Type 1 Diabetes:',danger)
    print('-----------------------------------------------------')
    
     
