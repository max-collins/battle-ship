import random
class Board:
    def __init__(self):
        self.width = 8
        self.height = 8
        self.data = [['O' for i in range(self.width)] for j in range(self.height)]
        self.opp_data  = [['O' for i in range(self.width)] for j in range(self.height)]
        self.has_hot = False #mode for searching for a shot
        self.hot_zone = (0,0) #area to search around
        self.v5, self.v4, self.v3, self.v33, self.v2 = True, True, True, True, True #vals are True if that ship is not sunk
    
    def __repr__(self):
        s = ''                          
        for row in range(0, self.height): # The main board
            
            for col in range(0, self.width):
                s += self.data[row][col] 
            s = s + '|' + str(row) #add row numbers
            s += '\n'
        s += (self.width + 1) * '-'   # Bottom of the board
        
        s = s + '\n'
        for col in range(self.width):
            s = s + str(col) #put the column numbers underneath
        return s

    def show_opp_data(self):
        s = ''                          
        for row in range(0, self.height): # The main board
            
            for col in range(0, self.width):
                s += self.opp_data[row][col] 
            s = s + '|' + str(row) #add row numbers
            s += '\n'
        s += (self.width + 1) * '-'   # Bottom of the board
        
        s = s + '\n'
        for col in range(self.width):
            s = s + str(col) #put the column numbers underneath
        print(s)

    def can_place(self,r_0,c_0,r_1,c_1, s):
        """in: r_0 is start row, c_0 start column, r_1 end row, c_1 end column, s is ship length
           out: True is a boat can be placed there(no overlap and on board not diag), False else.
        """
        if r_0 < 0 or r_0 > 8: #initial board chekcs
            return False

        if c_0 < 0 or c_1 > 8:
            return False

        if r_1 < 0 or r_1 > 8:
            return False

        if c_1 < 0 or c_1 > 8:
            return False

        if r_0 == r_1:#not diag cause rows

            if abs(c_0 - c_1) != (s-1): #fits ship length
                return False

            c_lower = min(c_0,c_1)
            c_upper = max(c_0,c_1) #range doesnt work if the lower bound is higher
            for i in range(c_lower, c_upper): #no overlap
                if self.data[r_0][i] != 'O':
                    return False
            return True

        if c_0 == c_1: #not diag cause cols
            if abs(r_0 - r_1) != (s-1):#fits ship length
                return False
            r_lower = min(r_0,r_1)
            r_upper = max(r_0,r_1) #range doesnt work if the lower bound is higher
            for i in range(r_lower, r_upper): #no overlap
                if self.data[i][c_0] != 'O':
                    return False
            return True
        return False

    def can_place_for_opp(self,r_0,c_0,r_1,c_1, s):
        """can_place() but for ai_just_lookin
        """
        if r_0 < 0 or r_0 > 8: #initial board chekcs
            return False

        if c_0 < 0 or c_1 > 8:
            return False

        if r_1 < 0 or r_1 > 8:
            return False

        if c_1 < 0 or c_1 > 8:
            return False

        if r_0 == r_1:#not diag cause rows

            if abs(c_0 - c_1) != (s-1): #fits ship length
                return False

            c_lower = min(c_0,c_1)
            c_upper = max(c_0,c_1) #range doesnt work if the lower bound is higher
            for i in range(c_lower, c_upper): #no overlap
                if self.opp_data[r_0][i] != 'O':
                    return False
            return True

        if c_0 == c_1: #not diag cause cols
            if abs(r_0 - r_1) != (s-1):#fits ship length
                return False
            r_lower = min(r_0,r_1)
            r_upper = max(r_0,r_1) #range doesnt work if the lower bound is higher
            for i in range(r_lower, r_upper): #no overlap
                if self.opp_data[i][c_0] != 'O':
                    return False
            return True
        return False

    def place_aircraft_carrier(self, r, c):
        """I was just too lazy to do this command a bunch"""
        self.data[r][c] = "A"
    def place_battleship(self, r, c):
        """I was just too lazy to do this command a bunch"""
        self.data[r][c] = "B"
    def place_sub(self, r, c):
        """I was just too lazy to do this command a bunch"""
        self.data[r][c] = "S"
    def place_cruiser(self, r, c):
        """I was just too lazy to do this command a bunch"""
        self.data[r][c] = "C"
    def place_destroyer(self, r, c):
        """I was just too lazy to do this command a bunch"""
        self.data[r][c] = "D"

    def init_game(self):
        """initializes a board for the player to fill out"""
        #destroyer
        r_0 = int(input('start row for 5: '))
        c_0 = int(input('start col: '))
        r_1 = int(input('end row: '))
        c_1 = int(input('end col: '))
        while not self.can_place(r_0,c_0,r_1,c_1,5):
            r_0 = int(input('start row for 5: '))
            c_0 = int(input('start col: '))
            r_1 = int(input('end row: '))
            c_1 = int(input('end col: '))
        if r_0 == r_1:
            c_min = min(c_0,c_1)
            c_max = max(c_0,c_1)
            for i in range(c_min, c_max+1):
                self.place_aircraft_carrier(r_0,i)

        if c_0 == c_1:
            r_min = min(r_0,r_1)
            r_max = max(r_0,r_1)
            for i in range(r_min, r_max+1):
                self.place_aircraft_carrier(i,c_0)
        print(self)

        #whatever is under destroyer
        r_0 = int(input('start row for 4: '))
        c_0 = int(input('start col: '))
        r_1 = int(input('end row: '))
        c_1 = int(input('end col: '))
        while not self.can_place(r_0,c_0,r_1,c_1,4):
            r_0 = int(input('start row for 4: '))
            c_0 = int(input('start col: '))
            r_1 = int(input('end row: '))
            c_1 = int(input('end col: '))
        if r_0 == r_1:
            c_min = min(c_0,c_1)
            c_max = max(c_0,c_1)
            for i in range(c_min, c_max+1):
                self.place_battleship(r_0,i)

        if c_0 == c_1:
            r_min = min(r_0,r_1)
            r_max = max(r_0,r_1)
            for i in range(r_min, r_max+1):
                self.place_battleship(i,c_0)
        print(self)

        #under that idfk
        r_0 = int(input('start row for 3: '))
        c_0 = int(input('start col: '))
        r_1 = int(input('end row: '))
        c_1 = int(input('end col: '))
        while not self.can_place(r_0,c_0,r_1,c_1,3):
            r_0 = int(input('start row for 3: '))
            c_0 = int(input('start col: '))
            r_1 = int(input('end row: '))
            c_1 = int(input('end col: '))
        if r_0 == r_1:
            c_min = min(c_0,c_1)
            c_max = max(c_0,c_1)
            for i in range(c_min, c_max+1):
                self.place_cruiser(r_0,i)

        if c_0 == c_1:
            r_min = min(r_0,r_1)
            r_max = max(r_0,r_1)
            for i in range(r_min, r_max+1):
                self.place_cruiser(i,c_0)
        print(self)

        #happens twice
        r_0 = int(input('start row for 3: '))
        c_0 = int(input('start col: '))
        r_1 = int(input('end row: '))
        c_1 = int(input('end col: '))
        while not self.can_place(r_0,c_0,r_1,c_1,3):
            r_0 = int(input('start row for 3: '))
            c_0 = int(input('start col: '))
            r_1 = int(input('end row: '))
            c_1 = int(input('end col: '))
        if r_0 == r_1:
            c_min = min(c_0,c_1)
            c_max = max(c_0,c_1)
            for i in range(c_min, c_max+1):
                self.place_sub(r_0,i)
        

        if c_0 == c_1:
            r_min = min(r_0,r_1)
            r_max = max(r_0,r_1)
            for i in range(r_min, r_max+1):
                self.place_sub(i,c_0)
        print(self)

        #baby one
        r_0 = int(input('start row for 2: '))
        c_0 = int(input('start col: '))
        r_1 = int(input('end row: '))
        c_1 = int(input('end col: '))
        while not self.can_place(r_0,c_0,r_1,c_1,2):
            r_0 = int(input('start row for 2: '))
            c_0 = int(input('start col: '))
            r_1 = int(input('end row: '))
            c_1 = int(input('end col: '))
        if r_0 == r_1:
            c_min = min(c_0,c_1)
            c_max = max(c_0,c_1)
            for i in range(c_min, c_max+1):
                self.place_destroyer(r_0,i)

        if c_0 == c_1:
            r_min = min(r_0,r_1)
            r_max = max(r_0,r_1)
            for i in range(r_min, r_max+1):
                self.place_destroyer(i,c_0)
        print(self)

            
             
    def ai_board(self):
        while True:
            #destroyer
            r_0 = random.randrange(0,8)
            c_0 = random.randrange(0,8)
            r_1 = random.randrange(0,8)
            c_1 = random.randrange(0,8)
            while not self.can_place(r_0,c_0,r_1,c_1,5):
                r_0 = random.randrange(0,8)
                c_0 = random.randrange(0,8)
                r_1 = random.randrange(0,8)
                c_1 = random.randrange(0,8)
            if r_0 == r_1:
                c_min = min(c_0,c_1)
                c_max = max(c_0,c_1)
                if self.can_place(r_0,c_0,r_1,c_1, 5) == True:
                    for i in range(c_min, c_max+1):
                    
                        self.place_aircraft_carrier(r_0,i)

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                if self.can_place(r_0,c_0,r_1,c_1, 5) == True:
                    for i in range(r_min, r_max+1):
                    
                        self.place_aircraft_carrier(i,c_0)


            #whatever is under destroyer
            r_0 = random.randrange(0,8)
            c_0 = random.randrange(0,8)
            r_1 = random.randrange(0,8)
            c_1 = random.randrange(0,8)
            while not self.can_place(r_0,c_0,r_1,c_1,4):
                r_0 = random.randrange(0,8)
                c_0 = random.randrange(0,8)
                r_1 = random.randrange(0,8)
                c_1 = random.randrange(0,8)
            if r_0 == r_1:
                c_min = min(c_0,c_1)
                c_max = max(c_0,c_1)
                if self.can_place(r_0,c_0,r_1,c_1, 4) == True:
                    for i in range(c_min, c_max+1):
                    
                        self.place_battleship(r_0,i)

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                if self.can_place(r_0,c_0,r_1,c_1, 4) == True:
                    for i in range(r_min, r_max+1):
                    
                        self.place_battleship(i,c_0)

            #under that idfk
            r_0 = random.randrange(0,8)
            c_0 = random.randrange(0,8)
            r_1 = random.randrange(0,8)
            c_1 = random.randrange(0,8)
            while not self.can_place(r_0,c_0,r_1,c_1,3):
                r_0 = random.randrange(0,8)
                c_0 = random.randrange(0,8)
                r_1 = random.randrange(0,8)
                c_1 = random.randrange(0,8)
            if r_0 == r_1:
                c_min = min(c_0,c_1)
                c_max = max(c_0,c_1)
                if self.can_place(r_0,c_0,r_1,c_1, 3) == True:
                    for i in range(c_min, c_max+1):
                    
                        self.place_cruiser(r_0,i)

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                if self.can_place(r_0,c_0,r_1,c_1, 3) == True:
                    for i in range(r_min, r_max+1):
                    
                        self.place_cruiser(i,c_0)

            #happens twice
            r_0 = random.randrange(0,8)
            c_0 = random.randrange(0,8)
            r_1 = random.randrange(0,8)
            c_1 = random.randrange(0,8)
            while not self.can_place(r_0,c_0,r_1,c_1, 3):
                r_0 = random.randrange(0,8)
                c_0 = random.randrange(0,8)
                r_1 = random.randrange(0,8)
                c_1 = random.randrange(0,8)
            if r_0 == r_1:
                c_min = min(c_0,c_1)
                c_max = max(c_0,c_1)
                if self.can_place(r_0,c_0,r_1,c_1, 3) == True:
                    for i in range(c_min, c_max+1):
                        self.place_sub(r_0,i)
            

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                if self.can_place(r_0,c_0,r_1,c_1, 3) == True:
                    for i in range(r_min, r_max+1):
                        self.place_sub(i,c_0)

            #baby one
            r_0 = random.randrange(0,8)
            c_0 = random.randrange(0,8)
            r_1 = random.randrange(0,8)
            c_1 = random.randrange(0,8)
            while not self.can_place(r_0,c_0,r_1,c_1,2):
                r_0 = random.randrange(0,8)
                c_0 = random.randrange(0,8)
                r_1 = random.randrange(0,8)
                c_1 = random.randrange(0,8)
            if r_0 == r_1:
                c_min = min(c_0,c_1)
                c_max = max(c_0,c_1)
                if self.can_place(r_0,c_0,r_1,c_1, 2) == True:
                    for i in range(c_min, c_max+1):
                        self.place_destroyer(r_0,i)

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                if self.can_place(r_0,c_0,r_1,c_1, 2) == True:
                    for i in range(r_min, r_max+1):
                        self.place_destroyer(i,c_0)
            print(self)
            return

    def aiGuess(self):
        """Make a guess (random from list). Removes that guess from the list 
        so AI doesn't guess it again, and if there is a hit, then in the 
        next move it should check the four cardinal directions adjacent 
        to that point. (makes a list of those and choose randomly between them)
        Keeps guessing from those 4 directions until it gets another hit,
        which means it's figured out the orientation of the ship. Then check that
        direction and the direction on the opposite side (eg if north is a hit
        then check south as well, if east is a hit then check west as well) in case
        it hit in the middle of the ship. Keep guessing in those directions until
        it sinks the ship. Otherwise, if there has been no hit, then it guesses randomly."""
        
        
        list_HitTrue = []
        #Need a call to the hit register function here
        #Check if there's a hit, and look at the coordinates of that hit
        #If there is a hit, save the cardinal direction coordinates around that hit in a list: 
        #[(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        #Make a random guess from that list for the next move, and subtract that coordinate from 
        # both the mini-hit list and the overall available guesses list

        #else statement: if no move is advantageous (e.g. no hit), resort to random choice
        guess_location = random.choice(range(len(self.available_guesses)))
        guess = self.available_guesses[guess_location]
        print("I'll guess", guess, "!")
        self.available_guesses.remove(guess)
        return guess

    def take_shot(self, r, c):
        """in: r is a row c is a col
           out: mutates the board to an * if there's a hit, X otherwise, returns True if the r and c is a hit
        """
        if self.data[r][c] == 'S' or self.data[r][c] =='A' or self.data[r][c] =='B' or self.data[r][c] =='D' or self.data[r][c] =='C':
            self.data[r][c] = '*'
            self.opp_data[r][c] = '*'
            return True
        if self.data[r][c] == 'O':
            self.data[r][c] = 'X'
            self.opp_data[r][c] = 'X'
            return False
        return False
    
    def prob_density(self):
        """in: v5 true if destroyer isnt sunk, v4 if the four one isnt sunk, so on
           out: returns prob density of self.data by iterating ship placement across the board
        """
        denisty_graph = [[0 for i in range(self.width)] for j in range(self.height)]
        #destoryer
        if self.v5 == True:
            #with vert placement
            for i in range(self.width): #rows
                for j in range(self.height): #cols
                    if self.can_place_for_opp(i,j,i+(5-1), j,5):
                        for k in range(5-1):
                            denisty_graph[i+k][j] += 1
            #with horiz placement
            for i in range(self.width): #rows
                for j in range(self.height): #cols
                    if self.can_place_for_opp(i,j,i, j+(5-1),5):
                        for k in range(5-1):
                            denisty_graph[i][j+k] += 1
        

        #under that 
        if self.v4 == True:
            #with vert placement
            for i in range(self.width): #rows
                for j in range(self.height): #cols
                    if self.can_place(i,j,i+(4-1), j,4):
                        for k in range(4-1):
                            denisty_graph[i+k][j] += 1
            #with horiz placement
            for i in range(self.width): #rows
                for j in range(self.height): #cols
                    if self.can_place_for_opp(i,j,i, j+(4-1),4):
                        for k in range(4-1):
                            denisty_graph[i][j+k] += 1


        #hell if i know
        if self.v3 == True:
            #with vert placement
            for i in range(self.width): #rows
                for j in range(self.height): #cols
                    if self.can_place_for_opp(i,j,i+(3-1), j,3):
                        for k in range(3-1):
                            denisty_graph[i+k][j] += 1
            #with horiz placement
            for i in range(self.width): #rows
                for j in range(self.height): #cols
                    if self.can_place_for_opp(i,j,i, j+(3-1),3):
                        for k in range(3-1):
                            denisty_graph[i][j+k] += 1

        #under that
        if self.v33 == True:
            #with vert placement
            for i in range(self.width): #rows
                for j in range(self.height): #cols
                    if self.can_place_for_opp(i,j,i+(3-1), j,3):
                        for k in range(3-1):
                            denisty_graph[i+k][j] += 1
            #with horiz placement
            for i in range(self.width): #rows
                for j in range(self.height): #cols
                    if self.can_place_for_opp(i,j,i, j+(3-1),3):
                        for k in range(3-1):
                            denisty_graph[i][j+k] += 1


        #lil baby
        if self.v2 == True:
            #with vert placement
            for i in range(self.width): #rows
                for j in range(self.height): #cols
                    if self.can_place_for_opp(i,j,i+(2-1), j,2):
                        for k in range(2-1):
                            denisty_graph[i+k][j] += 1
            #with horiz placement
            for i in range(self.width): #rows
                for j in range(self.height): #cols
                    if self.can_place_for_opp(i,j,i, j+(2-1),2):
                        for k in range(2-1):
                            denisty_graph[i][j+k] += 1
        return denisty_graph

    def ai_just_lookin(self):
        """shoots at the highest num of the prob density graph"""
        max_val = (0,0,0) #thriple containing (val of prob density at (x,y),x,y)
        for i in range(len(self.prob_density())):
            for j in range(len(self.prob_density()[i])):
                max_val = max(max_val, (self.prob_density()[i][j], i, j))
        return (max_val[1],max_val[2])
    
    def ai_move(self):
        if not self.has_hot:
            shot = (self.ai_just_lookin()[0],self.ai_just_lookin()[1])
            if self.take_shot(shot[0],shot[1]):
                self.has_hot = True
                self.hot_zone = shot
                print('hit')
    
    
    

    def sunk_ship(self):
        if "A" not in repr(playerBoard): 
            print("They have sunk your aircraft carrier")
            return True
        
        if "A" not in repr(aiBoard):
            print("You have sunk their aircraft carrier")
            return True

        if "B" not in repr(playerBoard): 
            print("They have sunk your battleship")
            return True

        if "B" not in repr(aiBoard):
            print("You have sunk their battleship")
            return True

        if "C" not in repr(playerBoard): 
            print("They have sunk your cruiser")
            return True
        
        if "C" not in repr(aiBoard):
            print("You have sunk their cruiser")
            return True

        if "S" not in repr(playerBoard): 
            print("They have sunk your submarine")
            return True
        
        if "S" not in repr(aiBoard):
            print("You have sunk their submarine")
            return True

        if "D" not in repr(playerBoard): 
            print("They have sunk your destroyer")
            return True
            
        if "D" not in repr(aiBoard):
            print("You have sunk their destroyer")
            return True
    

def host_game():
    """runs the game"""
    print("Welcome to Battleship! Please place your ships.")
    playerBoard = Board()
    aiBoard = Board()
    playerhits = Board()
    aiBoard.ai_board()
    playerBoard.init_game()
    print(aiBoard)
    print('Your Targets')
    print(aiBoard.show_opp_data())
        
    while True: 
        #user takes a shot at the AI 
        user_shot_row = int(input("Which row would you like to target? "))
        user_shot_col = int(input("Which column would you like to target? "))

        shot = aiBoard.take_shot(user_shot_row, user_shot_col)
        #print("Your Ships")
        #print(playerBoard)
        print(' ')
        
        #Ai takes a shot at the player
        ai_shot_row = playerBoard.ai_just_lookin()[0]
        ai_shot_col = playerBoard.ai_just_lookin()[1]
        ai_shot = playerBoard.take_shot(ai_shot_row, ai_shot_col)
        playerhits.take_shot(ai_shot_row, ai_shot_col)
        print(' ')
        print("Your Ships")
        print(playerBoard)
        if ai_shot == True:
            print("You were hit at", ai_shot_row, ai_shot_col)
        else:
            print("Your opponent missed!")
        if playerBoard.sunk_ship() == True:
            print(playerBoard.sunk_ship())

        print(' ')
        print('Your Targets')
        print(aiBoard.show_opp_data())
        #print("Your Targets")
        #print(aiBoard.show_opp_data())
        if shot == True:
            print('You got a hit!')
            print(' ')
        else:
            print('You missed. Better luck next time!')
        if aiBoard.sunk_ship() == True:
            print(aiBoard.sunk_ship())

        if "B" and "A" and "S" and "C" and "D" not in repr(playerBoard): 
            print("They have sunk all of your ships. You have lost. Play again?")
            return
        
        elif "B" and "A" and "S" and "C" and "D" not in repr(aiBoard):
            print("You have sunk all of their ships. Congratulations! Play again?")
            return

    def ai_move(self):
        if not self.has_hot:
            shot = (self.ai_just_lookin()[0],self.ai_just_lookin()[1])
            if self.take_shot(shot[0],shot[1]):
                self.has_hot = True
                self.hot_zone = shot
                print('hit')
        else:
            pass



#peepin data functions
def lol_how_fast(N):
    data = []
    for i in range(N):
        b = Board()
        b.ai_board()
        count = 1
        while True:
            if b.take_shot(b.ai_just_lookin()[0], b.ai_just_lookin()[1]):
                break
            count += 1
        data.append(count)
    return data

def lol_how_fast_vis(N):
    data = []
    for i in range(N):
        b = Board()
        b.ai_board()

        count = 1
        while True:
            shot = b.take_shot(b.ai_just_lookin()[0], b.ai_just_lookin()[1])
            print(b.opp_data)
            print(shot)
            if shot:
                break
            count += 1
        data.append(count)
    return data


    

            












#peepin data functions
def lol_how_fast(N):

    data = []
    for i in range(N):
        b = Board()
        b.ai_board()
        count = 1
        while True:
            if b.take_shot(b.ai_just_lookin()[0], b.ai_just_lookin()[1]):
                break
            count += 1
        data.append(count)
    return data

def lol_how_fast_vis(N):

    data = []
    for i in range(N):
        b = Board()
        b.ai_board()

        count = 1
        while True:
            shot = b.take_shot(b.ai_just_lookin()[0], b.ai_just_lookin()[1])
            print(b.opp_data)
            print(shot)
            if shot:
                break
            count += 1
        data.append(count)
    return data



