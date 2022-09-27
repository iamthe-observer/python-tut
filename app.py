# weight = float(input(':: '))
# form = str('(K)g or (L)bs: ')
# if form.upper() == 'K':
#    converted = weight / 0.45
#    print('weight in lbs: ' + str(converted))
# else:
#    converted = weight * 0.45
#    print('weight in lbs: ' + str(converted))

todos = []


def input_todo():
    inp = str(input('Enter Todo: '))
    answer = str(input('save?: Y / N:'))
    if answer.upper() == 'Y':
        todos.append(inp)
        print('the Todos are: ' + str(todos))
        re_inp = str(input('enter more? Y / N: '))
        if re_inp.upper() == 'Y':
            input_todo()
        else:
          print('bye!')
    elif answer.upper() == 'N':
        print('Did Not Save Boss...')
    else:
        print('Dont know what that means there buckoo...')


input_todo()