def pilhas(exp):
    pratos = []
    for i in range(len(exp)):
        if '(' in exp[i]:
            pratos.append('(') #Right plate!
        elif ')' in exp[i]:
            if len(pratos) > 0:
                topo = pratos.pop(-1) #Removing plate - LIFO Mode.
            else:
                pratos.append(')') #force error
    
    if len(pratos) == 0:
        print('Stack of finished dishes') #No more stack of plates.
        print(pratos)
    else:
        print('Wrong Position!') #Wrong Position.
        print(pratos)

#MAIN    
play = 'Y'
while play == 'Y':
    exp = input('Enter an expression with parentheses for the dishes: ')
    if '(' not in exp and ')' not in exp:
        print('Error')
        print()
    else:
        pilhas(exp)
        print()
    
    print('Do you want to try again? Y or N')
    play = input('Choose Your Option: ').upper()
    if play == 'N':
        print('End of Game!')
        break