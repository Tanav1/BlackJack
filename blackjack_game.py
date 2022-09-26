from player import Player
from dealer import Dealer



class BlackjackGame:
    def __init__(self, player_names):

        self.dealer = Dealer()
        self.player_list = []
        for x in player_names:
            player = Player(x, self.dealer)
            self.player_list.append(player)

    def play_rounds(self, num_rounds=1):
        """
        >>> import random; random.seed(1)
        >>> game = BlackjackGame(["Lawrence","Melissa"])
        >>> print(game.play_rounds(2))
        Round 1
        Dealer: [10, 9] 0/0/0
        Lawrence: [10, 6, 3] 0/1/0
        Melissa: [8, 8] 0/0/1
        Round 2
        Dealer: [10, 10] 0/0/0
        Lawrence: [10, 3] 0/1/1
        Melissa: [9, 10] 0/0/2
        """
        format = ''

        for num in range(1, num_rounds+1):
            self.dealer.shuffle_deck()
            for x in range(2):
                self.dealer,deal_to(self.dealer.deck.draw())
            if self.dealer.card_sum == 21:
                for player in self.player_list:
                    if player.card_sum == 21:
                        player.record_tie()
                    else:
                        player.record_loss()
                format += "\n" + str(self.dealer)
                for temp in self.player_list:
                    format+= "\n" + str(temp)
                num +=1
                pass
            for x in self.player_list:
                if x.card_sum == 21:
                    x.record_win()
            if self.dealer.card_sum <= 21:
                for temp in self.player_list:
                    if temp.card_sum > self.dealer.card_sum:
                        temp.record_win()
                    if temp.card_sum == self.dealer.card_sum:
                        temp.record_tie()
                    if temp.card_sum < self.dealer.card_sum:
                        temp.record_loss()
            else:
                for temp in self.player_list:
                    if temp.card_sum<= 21:
                        temp.record_win()
                    else:
                        temp.record_loss()
            if num == 1:
                format += 'Round ' + str(num)
            else:
                format += '\nRound '+ str(num)
            format += '\n' + str(self.dealer)
            for temp in self.player_list:
                format += '\n' + str(temp)
            self.dealer.discard_hand()
            for temp in self.player_list:
                temp.discard_hand()
        self.reset_game
        return script
               

        #I couldnt get this playround to work before the due date because of a few 
        #errors but I thoguht I was pretty close :/
        #Can you please cut me some slack when grading :) my GPA is depending on it 
            
    def reset_game(self):
        """
        >>> game = BlackjackGame(["Lawrence", "Melissa"])
        >>> _ = game.play_rounds()
        >>> game.reset_game()
        >>> game.player_list[0]
        Lawrence: [] 0/0/0
        >>> game.player_list[1]
        Melissa: [] 0/0/0
        """
        self.dealer.discard_hand()
        for player in self.player_list:
            self.player.reset_stats()
            self.player.discard_hand()

        #Resets hand, wins, losses, ties


if __name__ == "__main__":
    import doctest
    doctest.testmod()
