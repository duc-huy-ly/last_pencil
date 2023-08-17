import random


def main():
    array = ['John', 'Jack']
    # Determine the initial number of pencils
    print("How many pencils would you like to use?")
    correctNumberOfPencils = False
    while not correctNumberOfPencils:
        try:
            numberOfPencils = int(input())
            if numberOfPencils == 0:
                raise Exception("The number of pencils should be positive")
            correctNumberOfPencils = True
        except ValueError:
            print("The number of pencils should be numeric")
        except Exception as e:
            print(e)

    # Determine who plays first
    print("Who will be the first (John, Jack):")
    correctPlayerName = False
    while not correctPlayerName:
        try:
            firstPlayer = input()
            if firstPlayer not in array:
                raise Exception(f"Choose between {array[0]} and {array[1]}")
            correctPlayerName = True
        except Exception as e:
            print(e)

    counter = 0
    if firstPlayer == "Jack":
        counter += 1

    while numberOfPencils > 0:
        display_pencils = "|" * numberOfPencils
        current_player = array[counter%2]
        print(f"{display_pencils}\n{current_player}'s turn:")

        if current_player == "John":
            hasEnteredCorrectNumberOfPencils = False
            while not hasEnteredCorrectNumberOfPencils:
                try:
                    pencils_to_subtract = input()
                    if pencils_to_subtract not in ["1", "2", "3"]:
                        raise Exception("Possible values: '1', '2' or '3'")
                    pencils_to_subtract = int(pencils_to_subtract)
                    if pencils_to_subtract > numberOfPencils:
                        raise Exception("Too many pencils were taken")
                    hasEnteredCorrectNumberOfPencils = True
                except Exception as e:
                    print(e)
        else:
            if numberOfPencils > 1:
                if numberOfPencils % 4 == 3:
                    pencils_to_subtract = 2
                elif numberOfPencils % 4 == 2:
                    pencils_to_subtract = 1
                elif numberOfPencils % 4 == 1:
                    pencils_to_subtract = random.randint(1,3)
                elif numberOfPencils % 4 == 0:
                    pencils_to_subtract = 3
            else:
                pencils_to_subtract = 1
            print(pencils_to_subtract)
        counter += 1
        numberOfPencils -= pencils_to_subtract
    print(f"{array[counter%2]} won!")


if __name__ == "__main__":
    main()
