'''
Arfan Danial Bin Zainal Abidin, 20284997
Chau Lindon, 20284682

Question No.4
'''

import symptoms

def main():
    retry='Y'
    while retry.upper()=='Y':
        print('\n')
        print('-----------------------------------------------------------')        
        print('-----------      Test for Type 1 Diabetes     -------------')
        print('-----------------------------------------------------------')
        print('You are required to answer these question to determine risk')
        print('Follow the digit under each question to answer the question')
        symptoms.getSymp()
        retry=input('Do you want to retry? Y-yes  other keys-No: ')
        
        if retry.upper()!='Y':
            print('\nStay Healthy')
            print('and Have a nice day!')
            break
        else:
            continue


main()
            
        
    
