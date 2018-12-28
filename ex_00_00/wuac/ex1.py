# Napisz funkcję, która będzie prostą wersją gry „Kamień, papier, nożyce”. Może to być wersja polska lub angielska. Funkcja jako argumenty przyjmuje dwa stringi („kamień”, „papier” lub „nożyce”), a następnie w formie alertu podaje wynik (czyli np. wypisuje „Gracz nr 1 wygrał” – zakładamy, że gracz numer 1 to osoba, która podała pierwszy string). Jeśli do funkcji zostanie podany nieodpowiedni argument, tj. taki, który nie jest ani kamieniem, ani papierem, ani nożycami, poinformuj o tym gracza wyświetlając alert z tekstem.

usr1_choice = input('User 1: rock, paper or scissors?')
usr2_choice = input('User 2: rock, paper or scissors?')
if usr1_choice == usr2_choice:
    print("It's a draw!")
else:
    if usr1_choice == 'rock':
        if usr2_choice == 'paper':
            print('User 2 wins!')
        if usr2_choice == 'scissors':
            print('User 1 wins!')
    elif usr1_choice == 'paper':
        if usr2_choice == 'scissors':
            print('User 2 wins!')
        if usr2_choice == 'rock':
            print('User 1 wins!')
    elif usr1_choice == 'scissors':
        if usr2_choice == 'rock':
            print('User 2 wins!')
        if usr2_choice == 'paper':
            print('User 1 wins!')
