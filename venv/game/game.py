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
    
    def oppsite_player(self,player):
        if player == 'Player 1':
            return 'Player 2'
        else:
            return 'Player 1'
    
    def get_possible_moves(self,player):
        player_hands  = []
        oppsite_hands = []
        for k,v in self.state[player].items():
            if v < 5:
                player_hands.append(k)
        for k,v in self.state[self.oppsite_player(player)].items():
            if v < 5:
                oppsite_hands.append(k)
        moves = {}
        n=1
        for i in range(len(player_hands)):
            for j in range(len(oppsite_hands)):
                moves.update({n: player + ' ' + player_hands[i] + ' touches ' + self.oppsite_player(player) + ' ' + oppsite_hands[j]})
                n += 1
        return moves
    
    def make_move(self, move):
        pass
            
   
    
       