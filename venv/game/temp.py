state = { 'Player 1': {'right_hand': 1,'left_hand':1},'Player 2': {'right_hand': 1}}      
def get_possible_moves(state):
    moves = {'Player 1':[],'Player 2':[]}
    hands ={}
    for k,v in state.items():
        hands.update({k:list(v.keys())})
    print(hands)
    for item in hands['Player 1']:
        moves['Player 1'].append({item:hands['Player 2']})
    for item in hands['Player 2']:
        moves['Player 2'].append({item:hands['Player 1']})
    print(moves)
    return moves

get_possible_moves(state)