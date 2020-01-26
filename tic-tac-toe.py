import numpy as np

class player:
    def __init__(self):
        return

    def take_action(self, env):
        return

    def update(self):
        return

class environment:
    def __init__(self):
        self.LENGTH = 3
        self.board = np.zeros((self.LENGTH, self.LENGTH))
        self.x = -1
        self.o = 1
        self.winner = None
        self.ended = False
        self.num_states = 3**(self.LENGTH*self.LENGTH)

    def is_empty(self,i,j):
        return self.board[i,j] == 0

    def reward(self, sym):
        if not self.game_over():
            return 0

        return 1 if self.winner == sym else 0

    def get_state(self):
        k = 0
        h = 0
        for i in range(self.LENGTH):
            for j in range(self.LENGTH):
                if self.board[i,j] == 0:
                    v = 0
                elif self.board[i,j] == self.x:
                    v = 1
                elif self.board[i,j] == self.o:
                    v = 2
                h += (3**k) * v
                k += 1
        return h

    def game_over(self, force_recalculate = False):
        if not force_recalculate and self.ended:
            return self.ended

        for i in range(self.LENGTH):
            for player in (self.x, self.o):
                if self.board[i].sum() == player * self.LENGTH:
                    self.winner = player
                    self.ended = True
                    return True

        for j in range(self.LENGTH):
            for player in (self.x, self.o):
                if self.board[:,j].sum() == player * self.LENGTH:
                    self.winner = player
                    self.ended = True
                    return True

        for player in (self.x, self.o):
            if self.board.trace() == player * self.LENGTH:
                self.winner = player
                self.ended = True
                return True

            if np.fliplr(self.board).trace() == player * self.LENGTH:
                self.winner = player
                self.ended = True
                return True

            if np.all((self.board == 0) == False):
                self.winner = None
                self.ended = True
                return True

            self.winner = None
            return False


    def draw_board(self):
        for i in range(self.LENGTH):
            print("____________")
            for j in range(self.LENGTH):
                print(" "),
                if self.board[i,j] == self.x:
                    print("x")
                elif self.board[i,j] == self.o:
                    print("o"),
                else:
                    print(" ")
                    print("")
                print("____________")


def play_game(a1,a2,env):
    # change player
    player = a1

    while not env.game_over():
        if player == a1:
            player = a2
        if player == a2:
            player = a1

        player.take_action(env)
        state = env.get_state()
        a1.update(state)
        a2.update(state)

