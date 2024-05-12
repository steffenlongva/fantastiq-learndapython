print(
    '''
*******************************************************************************
   _ _ _ _ _                                                                  
  ( " " " " )                    .gggppp.                                     
   l       :                    :$P_  _T$;                                    
   |       |                    (  ,  .  )                                    
   |      _|                     ; '--' :                                     
   |_   _/ l)_                   ;  -- ):                                     
   |(""" `-'  l                  "------"t-.                         ___      
   |-'      _.'                 /"j-.-,t' \ \                   .-.C'   "..'  
   |        ;                  / .^./ :_"-.\ ;                  ;' ;":--._;-  
   :        :      .'.  ______j____J____t___Lj________          :_ :_;   ))   
   :"-.__    t  .-.|  ;/       ,-+. ,-----.           \         : "      ";   
   :"--._"""/ \/  :\ //        :  : |      \           \   _____;C   )    ;   
  .;     ""-`t'\.'\\Y/          ""  |_______;          _j / _| /-.-._____:    
 / ;      `. '-/ _///  ,--------.   |_     _:         /  """jj'/-/.____.-:    
: :   \     ;.' /\"y  /         /l  |-"""""-;        /      : / /_  .     ;-. 
; :    \   /   /  /  /_        / ;   """""""        :    ___:/ // )'      :  ;
; ;     \.'"--'  /   \ """""--: /                   |"""" _.; /(.-\    /  :  :
; ;             /    /""""---(|/                    | )--|  """"_.-`..'   ;  :
; :            /     """""----'                     '--..'--""t"         :   ;
:  ;          /                                                \         ;  : 
 ; :.__      /                                                  \       /   ; 
 :  `^$$$pppy                                                    tp._.gj   /  
  `.   "^$$P                                                      T$$^'  .'   
    ""--._/ bug                                                    \__.-"  
*******************************************************************************
'''
)

print("Welcome to Ila Hardcore Gaming Island.")
print("Your mission is to win the game.")
choice1 = input(
    'You\'re at a crossroad, which direction do you want to go? Type "left" or "right".'
).lower()

if choice1 == "left":
    choice2 = input(
        'You have arrived at a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
    ).lower()
    if choice2 == "wait":
        choice3 = input(
            "You arrive at the front of the castle. The castle has 3 doors. One red, one yellow and one blue. Which colour do you choose?"
        ).lower()
        if choice3 == "red":
            print("The room is full of death. Game Over.")
        elif choice3 == "yellow":
            print("The door smashes your face. Game Over.")
        elif choice3 == "blue":
            print("You enter the castle! You Win the game!")
    else:
        print("You are bad at swimming and drowned. Game Over.")
else:
    print("You fell of a cliff and broke it all. Game Over.")
