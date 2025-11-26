import random;

while True:
   ans = input('Would you like to continue (y/n): ').lower();
   if ans == 'y' :
     die1 = random.randint(1,6);
     die2 = random.randint(1,6);
     print(die1,die2);
   elif ans == 'n':
     print('Thanks for playing !!');
     break
   else:
     print('Invalid choice !!');