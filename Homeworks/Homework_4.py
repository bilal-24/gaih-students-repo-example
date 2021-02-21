# I have some copy but, googling must count as a coding skill. It is like using a module...
# However, it contains many bug fixes and my original codes

from random import choice

class Man:

    man = (
        """
         ------
         |    |
         |
         |
         |
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    O
         |
         |
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    O
         |   -+-
         | 
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-
         |   
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-/
         |   
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-/
         |    |
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-/
         |    |
         |    |
         |   | 
         |   | 
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-/   
         |    |
         |    |
         |   | |
         |   | |
         |  
        ----------
        """) # the best tuple that i saw...

    WORDS = ("ARTIFICIAL", "INTELLIGENCE", "PYTHON", "DEEP", "MACHINE", "LEARNING")

    def __init__(self):

        self._word = choice(self.WORDS)
        self._so_far = "-" * len(self._word)
        self._used = []
        self._wrong_answers = 0

    
    def play(self):

        self.__init__()

        while self._wrong_answers < len(self.man) and (self._so_far != self._word):
            self.current_progress()
            guess = self.user_guess()
            self.checking(guess)

        self.result()
        self._play_again()


    def checking(self, guess):

        if guess in self._word:
            print("\nWell Done!")

            for i in range(len(self._word)):
                if guess == self._word[i]:

                    self._so_far = self._so_far[:i] + guess + self._so_far[i+1:]
                    # This is a copy because, it necessitates some more practise for me!!!

        else:
            print("\nINCORRECT! Try again!")
            self._wrong_answers += 1

    
    def _play_again(self):

        print("\nWould you like to play again?\n")
         
        while True:                 # We can input either 'Y' or 'N' anymore... Otherwise, back to square one...
            
            user_input = input("Enter Y for yes or N for no: ").upper()
            
            if user_input == "Y":
                self.play()
                break

            elif user_input == "N":
                print("\nThank you for playing!\n")
                break

            else:
                print("Invalid Entry!!!")
                
    
    def current_progress(self):

        print("\n",self.man[self._wrong_answers])
        print("\nWord so far: ", self._so_far)
        print("\nLetters used: ", sorted(self._used))

    
    def result(self):

        if self._wrong_answers == len(self.man):
            print("\nLooser!")
        else:
            print("\nCongratulations!\n")
            print("The Word: ",self._word)     # Eventually, We can see full word...


    def user_guess(self):

        while True:         # I blocked multiple letters input...
            
            guess = input("Guess a letter: ").upper() 
            
            if len(guess) == 1:                         
                break
            else:
                print("\nPLEASE, ENTER ONE LETTER!!!")
                continue

        while guess in self._used:
            print("\nTry again... You've already used this letter")
            guess = input("Guess a letter: ").upper()

            print()

        self._used.append(guess)

        return guess


game = Man()
game.play()

