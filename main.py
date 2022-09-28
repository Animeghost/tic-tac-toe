import random

table=[[1,2, 3],[4,5, 6],[7,8, 9]]
comp_moves=[1,2,3,4,5,6,7,8,9]

for row in table:
    print(row)
def user_move():
    global comp_moves
    user = int(input('where do you want to put your next sign \n'))
    while user not in comp_moves:
        user = int(input('please use a number still left on the table \n'))
    
    for row in table:
        for number in row:
            if number == user:
                point=row.index(number)
                row[point]='O'
                comp_moves.remove(user)
                
        print(row)


def comp_turn():
    comp=random.choice(comp_moves)  
    for row in table:
        for number in row:
            if number == comp:
                point=row.index(number)
                row[point]= 'X'
                comp_moves.remove(comp)
        print(row)
    return comp

def win(point):
    if table[0][0] == table[0][1] == table[0][2] ==point:
        return True
    elif table[1][0] == table[1][1] == table[1][2] ==point:
        return True
    elif table[0][0] == table[1][1] == table[2][2] ==point:
        return True
    elif table[0][2] == table[1][1] == table[2][0] ==point:
        return True
    elif table[0][0] == table[1][0] == table[2][0] ==point:
        return True
    elif table[0][1] == table[1][1] == table[2][1] ==point:
        return True
    elif table[0][2] == table[1][2] == table[2][2] ==point:
        return True
    elif table[2][0] == table[2][1] == table[2][2] == point:
        return True
    return False

        
turns=True

while turns is True:
    
    user_move()
    
    if win(point='O') == True:
        print('you win')
        turns=False
    
    if len(comp_moves) == 0:
        print("Too bad folks it's a draw")
        turns=False
    else:
        comp_turn()
        
        if win(point='X') == True:
            turns=False
            print('You lose')
    

