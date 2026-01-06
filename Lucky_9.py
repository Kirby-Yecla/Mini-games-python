import secrets
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def lucky_9():
    clear()
    play = 'y'
    wins_comp=0
    wins_user=0
    suits= ["Clubs", "Diamonds", "Hearts", "Spades"]
    deck_cards = {"Ace": 1, 
                2:2,
                3:3,
                4:4,
                5:5,
                6:6,
                7:7,
                8:8,
                9:9,
                "King":0,
                "Queen": 0,
                "Jack": 0}

    while play == 'y':
        print("WELCOME TO LUCKY 9")

        options= list(deck_cards.keys())

        card1_comp= secrets.choice(options)
        card2_comp= secrets.choice(options)
        s1c= secrets.choice(suits)
        s2c= secrets.choice(suits)

        card1_user= secrets.choice(options)
        card2_user= secrets.choice(options)
        s1u= secrets.choice(suits)
        s2u= secrets.choice(suits)


        value1_comp= deck_cards[card1_comp]
        value2_comp= deck_cards[card2_comp]
        value1_user= deck_cards[card1_user]
        value2_user= deck_cards[card2_user]

        total_comp= (value1_comp + value2_comp) % 10
        total_user= (value1_user + value2_user) % 10

        print(f"Card 1: {card1_user} of {s1u}\nCard 2: {card2_user} of {s2u}\nTotal: {total_user}")
        time.sleep(1)
        
        hit= str(input("\nHit it?[y/n]: ")).lower()
        
        card3_info= ""

        if total_comp <=8:
            card3_comp= secrets.choice(options)
            value3_comp= deck_cards[card3_comp]
            s3c= secrets.choice(suits)
            total_comp= (value1_comp + value2_comp + value3_comp) % 10
            card3_info= f"\nCard 3: {card3_comp} of {s3c}" 
            
        if hit == 'y':
            card3_user= secrets.choice(options)
            value3_user= deck_cards[card3_user]
            s3u= secrets.choice(suits)
            total_user= (value1_user + value2_user + value3_user) % 10
            time.sleep(1)
            print(f"\nCard 3: {card3_user} of {s3u}\nTotal: {total_user}")
        
        
        if total_user> total_comp:
            print("You win")
            if total_comp == 9:
                print("A LUCKY 9!!")
            print(f"\nComputer's card:\nCard 1: {card1_comp} of {s1c}\nCard 2: {card2_comp} of {s2c}{card3_info}\nTotal: {total_comp} ")
            wins_user+=1
        elif total_user<total_comp:
            print("The computer wins\n")
            print(f"Computer's card:\nCard 1: {card1_comp} of {s1c}\nCard 2: {card2_comp} of {s2c}{card3_info}\nTotal: {total_comp} ")
            if total_comp == 9:
                print("A LUCKY 9!!")
            wins_comp += 1
        
        else:
            print("Cards with same value\nIt's a tie\n")
            time.sleep(1)
            print(f"Computer's card:\nCard 1: {card1_comp} of {s1c}\nCard 2: {card2_comp} of {s2c}{card3_info}\nTotal: {total_comp} ")

        time.sleep(1)
        play = str(input("\nPlay again?[y/n]: "))
        
        if play == 'n':
            clear()
            print("Thank you for playing the game")
            print(f"Computer wins: {wins_comp}\nYour wins: {wins_user}")
            break
        clear()



lucky_9()
