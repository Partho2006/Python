import random;

c = ('r','p','s');
dic = {'r':'Rock', 'p':'Paper', 's':'Scissor'};

while True:
 choice = input('Rock, Paper, or Scissor? (r/p/s): ').lower(); 

 if (choice not in c):
    print('Invalid choice !');
    continue;
 comp_choice = random.choice(c);

 print(f'You chose {dic[choice]}');
 print(f'You chose {dic[comp_choice]}');

 if choice == comp_choice:
    print('draw !!');
 elif ( 
    (choice == 'r' and comp_choice == 's') or 
    (choice == 's' and comp_choice == 'p') or 
    (choice == 'p' and comp_choice == 'r') ):
      print('You win !!');
 else:
      print('You lose !!');

 user = input('Continue (y/n): ').lower();
 if user == 'n':
    break;
    print('Well Played !');
 else:
    continue;