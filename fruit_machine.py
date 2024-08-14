import random
MAX_LINES =3
MAX_BET =100
MIN_BET =1

ROWS = 4
COLUMNS =4

symbol_count ={
    "#":2,
    "@":4,
    "$":6,
    "#":8
}

#it is to determine how many times of the money will player get if they win.eg if # :2 in 1st line so if they win they will get 2 time the money
symbol_value ={
    "#":8,
    "@":6,
    "$":4,
    "#":2
}

def check_winings(COLUMNS,lines,bet,values):
    winings =0
    wining_lines=[]
    for line in range(lines):
        symbol =COLUMNS[0][line]
        for column in COLUMNS:
            symbol_to_check =column[line]
            if symbol != symbol_to_check:
                break
        else:
            winings +=values[symbol] * bet
            wining_lines.append(line + 1) 
            
    return winings,wining_lines
                

def slot_machine(ROWS,COLUMNS,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():# .items will give you both the key and the value associated with it.
        for _ in range(symbol_count):# _ anonymous veriable on python to itrate (symbol_count)times.
            all_symbols.append(symbol)
            
    cols =[]
    for _ in range(COLUMNS):
        column =[]
        current_symbols = all_symbols[:]
        for _ in range(ROWS):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
         
        cols.append(column)
               
    return cols

def print_slot_machine(cols):
    for row in range(len(cols[0])):
        for i, column in enumerate(cols):
            if i != len(cols)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
                
        print()
        
        
 #for entering the amount of total deposit.
def money():
    while True: #to take input again automitically when  wrong among is input
        amount = input("Enter the amount you want to deposit:")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater then 0.")
        else:
            print("please enter a number.")
            
    return amount

#for the no. of lines you want to bet on.
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on(1-"+str(MAX_LINES)+")?: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <=lines<=MAX_LINES :
                break
            else:
                print("enter a valid number of line.")
        else:
            print("please enter a number.")
            
    return lines

#for the amount you want to bet.
def get_bet():
    while True:
        bet = input("Enter the amount you want to bet:")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between {MIN_BET}-{MAX_BET}")
        else:
            print("Please enter a number.")

    return bet

def game(balance):
    lines=get_number_of_lines()
   
    #to check either the bet is less then the balance or not
    while True:
        
        bet=get_bet()
        total_bet=bet * lines
        if total_bet > balance:
            print(f"you don't have enough balance! Your current balance is: {balance}")
        else:
            break
    print(f"you are betting {bet} on {lines} lines.. ")
    print(f"Your toal bet will be: {total_bet}")
    slots = slot_machine(ROWS,COLUMNS,symbol_count)
    print_slot_machine(slots)
    winings,wining_lines =check_winings(slots,lines,bet,symbol_value)
    
    if winings > 0:
        print(f"you won :{winings}.")
        print(f"you won on line:{wining_lines}")
    else:
        print("YOU LOSE.")
        print("HAHAHAHA LOSER ")
    return winings -total_bet
    
            
def main():    
    balance= money()
    while True:
        print(f"your current balance is :{balance}")
        answer = input("press enter to play and q to quit.")
        if answer == "q":
            break
        balance += game(balance)
        
    print(f"Your remaining balance is:{balance}")
        
    
      
main()

 