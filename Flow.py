Age = int(input('Age:'))

if Age < 30 :
    print('Eat Pizza');
    
    Pizza = str(input('Yes or No:'))
    if Pizza == 'Yes':
        print('Fit')
    else:
        print('Unfit');
        
else:
    
    print('Exercise');
    
    Exercise =str(input('Yes or No:'))
    
    if Exercise == 'Yes':
        print('Fit');
        
    else:
        
        print('Unfit');
