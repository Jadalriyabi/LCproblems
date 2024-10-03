'''
Create a 2-player tennis game system. The system holds the score of the game, and returns the score when asked. The system can also update the score when one of the 2 players scores a point. 

A player wins when they reach >=4 points with a 2 point difference between the other player.


Part 2: Now instead of just printing out points like 1,2,3. We now want to print out the score like a real tennis game. Here are the scoring rules:
- 1 point means 15
- 2 points mean 30
- 3 points mean 40
- 4 points mean game
- If the score is 1-0, that means the score is "15 love"
- If the score is 2-0, that means the score is "30 love"
- If the score is 3-0, we should print "40 love"
- If the score is 2-1, we should print "30 15"
- If the scores are tied at 1-1, 2-2, we should say "15 all" or "30 all"
- If the scores are tied at 3-3, we should say "Deuce"
- If the scores are >3 without a 2point difference, we should say advantage player_name. E.g. if the score is 3-4, we should say "Advantage player 2"


Part 3: Now that we have built our tennis game which returns scores like a real tennis game, we also want to mimic tennis matches and games. A player can win several games, and a tennis match is over when a player wins 3 games

'''

class TennisGame:
    def __init__(self, player_1_name, player_2_name):
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.player_1_score = 0
        self.player_2_score = 0
        self.game_over = False #when true, game is over

    
    def get_score(self):
        #check if the game is over, return winner
        if self.game_over: 
            winner = self._check_for_winner()
            return f"Game Over! {winner} won."
        
        if self.player_1_score >= 3 and self.player_2_score >= 3:
            if self.player_1_score == self.player_2_score:
                return "Deuce"
            elif self.player_1_score == self.player_2_score + 1:
                return f"Advantage {self.player_1_name}."
            elif self.player_2_score == self.player_1_score + 1:
                return f"Advantage {self.player_2_name}."
        
        if self.player_1_score == self.player_2_score:
            if self.player_1_score == 0:
                return "Love all"
            return f"{self._format_score(self.player_1_score)} all"
        
        return f"{self._format_score(self.player_1_score)} {self._format_score(self.player_2_score)}"
    
    def _format_score(self, score):
        if score == 0:
            return "love"
        elif score == 1:
            return "15"
        elif score == 2:
            return "30"
        elif score == 3:
            return "40"
        
            
        
        
        # return f"NO WINNER YET.\n{self.player_1_name}: {self.player_1_score} \n{self.player_2_name}: {self.player_2_score} "
    
    def update_score(self, player):
        if self.game_over:
            print("Game is already over! No more points allowed")
            return
        
        #updating score based on who scored
        if player == self.player_1_name:
            self.player_1_score += 1
        elif player == self.player_2_name:
            self.player_2_score += 1

        self._check_for_winner()
    

    def _check_for_winner(self):
        #determining if player 1 won and return players 1's name
        if self.player_1_score >= 4 and self.player_1_score >= self.player_2_score + 2:
            self.game_over = True
            return self.player_1_name
        #determining if player 2won and return players 2's name
        elif  self.player_2_score >= 4 and self.player_2_score >= self.player_1_score + 2:
            self.game_over = True
            return self.player_2_name
        
        return "No Player has won yet"



game = TennisGame("Jad", "Ibrahim")
print(game.get_score())

game.update_score("Ibrahim")
print(game.get_score())
game.update_score("Jad")
print(game.get_score())
game.update_score("Ibrahim")
print(game.get_score())
game.update_score("Jad")
print(game.get_score())
game.update_score("Ibrahim")
print(game.get_score())
game.update_score("Jad")
print(game.get_score())
game.update_score("Ibrahim")
print(game.get_score())
game.update_score("Jad")
print(game.get_score())
game.update_score("Ibrahim")
print(game.get_score())
game.update_score("Ibrahim")
print(game.get_score())

game = TennisGame("Jad", "Ibrahim")
print(game.get_score())
game.update_score("Ibrahim")
print(game.get_score())
game.update_score("Ibrahim")
print(game.get_score())
game.update_score("Ibrahim")
print(game.get_score())
game.update_score("Ibrahim")
print(game.get_score())
game.update_score("Ibrahim")
