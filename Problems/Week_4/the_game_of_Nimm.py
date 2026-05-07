def main():

    total_stones= 20
    player_1 = 1
    player_2 = 2

    while total_stones > 0:
        print(f"There are {total_stones} stones left.")
        removed_stones= int(input(f"Player {player_1} would you like to remove 1 or 2 stones? "))
        
        while removed_stones>2:
            removed_stones = int(input("Please enter 1 or 2: "))
        total_stones = total_stones - removed_stones
        print()

        if total_stones<=0:
            winner=2
            break

        print(f"There are {total_stones} stones left.")
        removed_stones= int(input(f"Player {player_2} would you like to remove 1 or 2 stones? "))
        
        while removed_stones>2:
            removed_stones = int(input("Please enter 1 or 2: "))
        total_stones = total_stones - removed_stones
        # print()

        if total_stones<=0:
            winner=1
            break

    if winner == 1:
        print(f"Player {player_1} wins!")
    elif winner == 2:
        print(f"Player {player_2} wins!")


if __name__ == '__main__':
    main()