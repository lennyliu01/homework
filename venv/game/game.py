class Game:
    def __init__(self, is_player1_first: bool):
        self.is_player1_first = is_player1_first

    def get_current_player(self):
        if self.is_player1_first:
            return "Player 1"
        return "Player 2"

    def get_possible_moves(self):
        raise NotImplemented

    def make_move(self, move):
        raise NotImplemented

    def is_winner(self, player):
        raise NotImplemented


class SubtractSquare(Game):
    def __init__(self, is_player1_first, state):
        Game.__init__(self, is_player1_first)
        self.state = state

    def get_possible_moves(self):
        result = []
        for i in range(self.state+1):
            if 0 < i ** 2 <= self.state:
                result.append(i**2)
        return result

    def get_state(self):
        return self.state

    def make_move(self, move):
        if move not in self.get_possible_moves():
            return False
        self.state -= move
        self.is_player1_first = not self.is_player1_first
        return True

    def is_winner(self, player):
        if self.state > 0:
            return False
        if player == "Player 1" and self.is_player1_first:
            return False
        if player == "Player 2" and self.is_player1_first:
            return True
        if player == "Player 1" and not self.is_player1_first:
            return True
        if player == "Player 2" and not self.is_player1_first:
            return False

class Chopsticks(Game):
    def __init__(self, is_player1_first:bool):
        self.is_player1_first = is_player1_first
        self.state = { 'Player 1': {'right_hand': 1,'left_hand':1},'Player 2': {'right_hand': 1, 'left_hand':1}}
    
    def get_state(self):  #why get state
        return self.state
    
    def get_possible_moves(self):
        hands ={}
        for k,v in state.items():
            hands.update({k:list(v.keys())})
        # hands = dict{Player 1:[all hands]},{Player 2:[all hands]}}
        # example {'Player 1': ['right_hand', 'left_hand'], 'Player 2': ['right_hand']} 
        moves = {'Player 1':[],'Player 2':[]}
        for item in hands['Player 1']:
            moves['Player 1'].append({item:hands['Player 2']})
        for item in hands['Player 2']:
            moves['Player 2'].append({item:hands['Player 1']})
        return moves
        '''
        example 
        {
        'Player 1': [{'right_hand': ['right_hand']}, {'left_hand': ['right_hand']}], 
        'Player 2': [{'right_hand': ['right_hand', 'left_hand']}]
        }
        '''
    def make_move(self, move):
        #move = [player, player hand,opposite hand]
        increment = self.state[self.get_current_player][move[1]]
        self.is_player1_first = not self.is_player1_first
        self.state[self.get_current_player][move[2]] = increment+ self.state[opposite_player][move[2]]
        if self.state[self.get_current_player][move[2]] >= 5:
            self.state.pop([self.get_current_player][move[2]])

    def is_winner(self, player):
        if self.state[get_current_player] == None:
            return True
            
   
    
       