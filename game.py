#!/usr/bin/env python3
"""

Features:
- Numbers 0-9
- Action cards: Skip, Reverse, Draw Two
- Wild and Wild Draw Four
- Draw pile, discard pile
- Turn flow
- Simple input prompts
"""

import random

# ----- Card Setup -----
colors = ['Red', 'Blue', 'Green', 'Yellow']
numbers = [str(n) for n in range(0, 10)]
actions = ['Skip', 'Reverse', 'Draw Two']
wilds = ['Wild', 'Wild Draw Four']




# ----- Deck Functions -----
def create_deck():
    """Create a deck of UNO cards."""
    deck = []
    for color in colors:
        # Add number cards: one 0, two of 1-9
        deck.append(f"0 of {color}")
        for num in range(1, 10):
            deck.append(f"{num} of {color}")
            deck.append(f"{num} of {color}")
        # Add actions: two of each per color
        for action in actions:
            deck.append(f"{action} of {color}")
            deck.append(f"{action} of {color}")
            
            
    # Add wilds
    for _ in range(4):
        deck.append("Wild")
        deck.append("Wild Draw Four")
    random.shuffle(deck)
    return deck





def deal_cards(deck, num_players=2):
    """Deal 7 cards to each player."""
    hands = {f"Player {i+1}": [deck.pop() for _ in range(7)] for i in range(num_players)}
    discard_pile = [deck.pop()]  # start with one card
    return hands, discard_pile






# ----- Gameplay Functions -----
def is_valid_play(card, top_card):
    """Check if a card can be played on top of the current card."""
    return (card.split(' ')[-1] == top_card.split(' ')[-1] or
            card.split(' ')[0] == top_card.split(' ')[0] or
            'Wild' in card)





def print_hand(hand):
    for i, card in enumerate(hand):
        print(f"{i}: {card}")
        
        
        

def player_turn(player, hand, top_card, deck):
    """Handle a player's turn."""
    print(f"\n{player}'s turn:")
    print(f"Top card: {top_card}")
    print("Your hand:")
    print_hand(hand)
    
    
    
    

    # Determine playable cards
    valid_cards = [card for card in hand if is_valid_play(card, top_card)]
    if valid_cards:
        print("\nPlayable cards:")
        for card in valid_cards:
            print(card)
        choice = input("Choose a card to play by typing exact card, or 'd' to draw: ").strip()
        if choice.lower() == 'd':
            hand.append(deck.pop())
            print(f"{player} drew a card.")
            return top_card
        elif choice in valid_cards:
            hand.remove(choice)
            print(f"{player} played {choice}")
            # If wild, ask for color
            if 'Wild' in choice:
                new_color = input("Choose a color (Red/Blue/Green/Yellow): ").strip().title()
                choice = f"{new_color} {choice}"
            return choice
        else:
            print("Invalid choice, drawing a card instead.")
            hand.append(deck.pop())
            return top_card
    else:
        print("No playable cards. Drawing a card...")
        hand.append(deck.pop())
        return top_card




# ----- Main Game Loop -----
def play_game():
    deck = create_deck()
    hands, discard_pile = deal_cards(deck)
    top_card = discard_pile[0]
    print(f"Starting card: {top_card}")
    players = ['You', 'Computer']
    current_player = 0



    while True:
        player_name = players[current_player]
        hand = hands[f"Player {current_player+1}"]

        if player_name == 'You':
            top_card = player_turn(player_name, hand, top_card, deck)
        else:
            # Simple AI: play first valid card or draw
            playable = [c for c in hand if is_valid_play(c, top_card)]
            if playable:
                card = playable[0]
                hand.remove(card)
                print(f"\nComputer plays {card}")
                if 'Wild' in card:
                    color = random.choice(colors)
                    card = f"{color} {card}"
                    print(f"Computer chose color {color}")
                top_card = card
            else:
                hand.append(deck.pop())
                print("\nComputer draws a card.")
                
                

        # Check for winner
        if len(hand) == 0:
            print(f"\n{player_name} wins!")
            break

        current_player = (current_player + 1) % len(players)



if __name__ == "__main__":
    print("Welcome to Simple UNO!")
    print("Rules implemented: numbers 0-9, Skip, Reverse, Draw Two, Wild, Wild Draw Four.")
    play_game()
