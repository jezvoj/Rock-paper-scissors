import random, time, sys


## concepts to implement
## winning money, balance for ties

## setting up the RPS class
class RockPaperScissors:
    def __init__(self):
        self.player_choice = ''
        self.cpu_choice = ''
        self.possibilities = ['rock','paper','scissors']
        self.money = 5
        self.wager = 10
        
    ## welcoming the player
    def gametime_init(self):
        print('Time to play!')
        time.sleep(1)
        print('Select your weapon: rock/paper/scissors')
        
    ## saves the values for both player's and CPU's weapons
    def selection(self):
        player_choice = ''
        while player_choice not in self.possibilities:
            print('Please select a valid weapon.')
            player_choice = input('>')
        print(f"Player's choice is {player_choice}.")
        self.player_choice = player_choice

        print("CPU's choosing its weapon.")
        time.sleep(1)
        
        cpu_choice = self.possibilities[random.randint(0,2)]
        self.cpu_choice = cpu_choice

        time.sleep(1)

    def win_money(self):
        self.money += self.wager
        print(f"You won {self.wager}!")
        print(f"Your current balance is {self.money}.")

    def lose_money(self):
        self.money -= self.wager
        print(f"You lost {self.wager}!")
        print(f"Your current balance is {self.money}.")

    def check_money(self):
        if self.money <= 0:
            print('You went bankrupt.')
            sys.exit()
        

    ## comparing function for both weapons
    def comparison(self):
        if self.player_choice == 'rock':
            if self.cpu_choice == self.player_choice:
                print('Its a tie! You both had rocks!')
            elif self.cpu_choice == self.possibilities[1]:
                print(f'''The cpu got {self.cpu_choice} while you have {self.player_choice}. CPU therefore wins!''')
                self.lose_money()
            else:
                print(f'''The cpu got {self.cpu_choice} while you have {self.player_choice}. You win!''')
                self.win_money()
                
                
        elif self.player_choice == 'paper':
            if self.cpu_choice == self.possibilities[0]:
                print(f'''The cpu got {self.cpu_choice} while you have {self.player_choice}. You win!''')
                self.win_money()
            elif self.cpu_choice == self.player_choice:
                print(f'Its a tie! You both had papers!')
            else:
                print(f'''The cpu got {self.cpu_choice} while you have {self.player_choice}. CPU therefore wins!''')
                self.lose_money()
        elif self.player_choice == 'scissors':
            if self.cpu_choice == self.possibilities[0]:
                print(f'''The cpu got {self.cpu_choice} while you have {self.player_choice}. CPU therefore wins!''')
                self.lose_money()
            elif self.cpu_choice == self.possibilities[1]:
                print(f'''The cpu got {self.cpu_choice} while you {self.player_choice}. You win!''')
                self.win_money()
            else:
                print('Its a tie! You both had scissors!')
        else:
            print('There is a bug')
        

    ## function for launching another round
    def rerun(self):
        restart = input('Wanna play another game? yes/no \n')
        if restart == 'yes':
            print('ok')
            game.game_loop()
        elif restart == 'no':
            print("We won't play then.")
        else:
            print('Enter valid answer. yes/no')
            self.rerun()

    ## game loop function, wraps together all the aforementioned functions
    def game_loop(self):
        game.gametime_init()
        game.selection()
        game.comparison()
        game.check_money()
        game.rerun()              

game = RockPaperScissors()
game.game_loop()
