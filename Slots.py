import random


def slots():
    global Balance, Price
    Balance = Balance-Price
    number1 = random.randint(3, 6)
    number2 = random.randint(3, 6)
    number3 = random.randint(3, 6)

    if number1 == 6 and number2 == 6 and number3 == 6:
        Balance += 2000
        print("---------------")
        print("-[7️⃣][7️⃣][7️⃣]-")
        print("---------------")
        print("-You won 2000$-")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 6 and number2 == 6 and number3 == 5:

        print("---------------")
        print("-[7️⃣][7️⃣][bar]-")
        print("---------------")
        print("--You won 0$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 5 and number2 == 6 and number3 == 6:

        print("---------------")
        print("-[bar][7️⃣][7️⃣]-")
        print("---------------")
        print("--You won 0$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 6 and number2 == 5 and number3 == 6:

        print("---------------")
        print("-[7️⃣][bar][7️⃣]-")
        print("---------------")
        print("--You won 0$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 5 and number2 == 5 and number3 == 6:
        Balance += 25
        print("---------------")
        print("-[bar][bar][7️⃣]-")
        print("---------------")
        print("--You won 25$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 6 and number2 == 5 and number3 == 5:
        Balance += 25
        print("---------------")
        print("-[7️⃣][bar][bar]-")
        print("---------------")
        print("--You won 25$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 5 and number2 == 6 and number3 == 5:
        Balance += 25
        print("---------------")
        print("-[bar][7️⃣][bar]-")
        print("---------------")
        print("--You won 25$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == number2 and number2 == number3 and number3 == 4:
        Balance += 30
        print("---------------")
        print("-[🫐][🫐][🫐]-")
        print("---------------")
        print("--You won 30$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 4 and number2 == 6 and number3 == 4:
        Balance += 20
        print("---------------")
        print("-[🫐][7️⃣][🫐]-")
        print("---------------")
        print("--You won 20$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 4 and number2 == 4 and number3 == 6:
        Balance += 20
        print("---------------")
        print("--[🫐][🫐][7️⃣--")
        print("---------------")
        print("--You won 20$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 6 and number2 == 4 and number3 == 4:
        Balance += 20
        print("---------------")
        print("-[7️⃣][🫐][🫐]-")
        print("---------------")
        print("--You won 20$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 4 and number2 == 6 and number3 == 6:
        Balance += 10
        print("---------------")
        print("-[🫐][7️⃣][7️⃣]-")
        print("---------------")
        print("--You won 10$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 6 and number2 == 4 and number3 == 6:
        Balance += 10
        print("---------------")
        print("-[7️⃣][🫐][7️⃣]-")
        print("---------------")
        print("--You won 10$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 6 and number2 == 6 and number3 == 4:
        Balance += 10
        print("---------------")
        print("-[7️⃣][7️⃣][🫐]-")
        print("---------------")
        print("--You won 10$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == number2 and number2 == number3 and number3 == 3:
        Balance += 15
        print("---------------")
        print("-[🍒][🍒][🍒]-")
        print("---------------")
        print("--You won 15$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 3 and number2 == 6 and number3 == 3:
        Balance += 10
        print("---------------")
        print("-[🍒][7️⃣][🍒]-")
        print("---------------")
        print("--You won 10$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 3 and number2 == 3 and number3 == 6:
        Balance += 10
        print("---------------")
        print("-[🍒][🍒][7️⃣]-")
        print("---------------")
        print("--You won 10$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 6 and number2 == 3 and number3 == 3:
        Balance += 10
        print("---------------")
        print("-[7️⃣][🍒][🍒]-")
        print("---------------")
        print("--You won 10$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 3 and number2 == 6 and number3 == 6:
        Balance += 5
        print("---------------")
        print("-[🍒][7️⃣][7️⃣]-")
        print("---------------")
        print("--You won 5$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 6 and number2 == 3 and number3 == 6:
        Balance += 5
        print("---------------")
        print("-[7️⃣][🍒][7️⃣]-")
        print("---------------")
        print("--You won 5$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 6 and number2 == 6 and number3 == 3:
        Balance += 5
        print("---------------")
        print("-[7️⃣][7️⃣][🍒]-")
        print("---------------")
        print("--You won 5$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 5 and number2 == 5 and number3 == 5:
        Balance += 50
        print("---------------")
        print("[bar][bar][bar]")
        print("---------------")
        print("--You won 50$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 5 and number2 == 4 and number3 == 4:
        Balance += 20
        print("---------------")
        print("-[bar][🫐][🫐]-")
        print("---------------")
        print("--You won 20$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 4 and number2 == 4 and number3 == 5:
        Balance += 20
        print("---------------")
        print("-[🫐][🫐][bar]-")
        print("---------------")
        print("--You won 20$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 4 and number2 == 5 and number3 == 4:
        Balance += 20
        print("---------------")
        print("-[🫐][bar][🫐]-")
        print("---------------")
        print("--You won 20$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 5 and number2 == 5 and number3 == 4:
        Balance += 35
        print("---------------")
        print("-[bar][bar][🫐]-")
        print("---------------")
        print("--You won 35$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 4 and number2 == 5 and number3 == 5:
        Balance += 35
        print("---------------")
        print("-[🫐][bar][bar]-")
        print("---------------")
        print("--You won 35$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 5 and number2 == 4 and number3 == 5:
        Balance += 35
        print("---------------")
        print("-[bar][🫐][bar]-")
        print("---------------")
        print("--You won 35$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 3 and number2 == 3 and number3 == 5:
        Balance += 10
        print("---------------")
        print("-[🍒][🍒][bar]-")
        print("---------------")
        print("--You won 10$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 3 and number2 == 5 and number3 == 3:
        Balance += 10
        print("---------------")
        print("-[🍒][bar][🍒]-")
        print("---------------")
        print("--You won 10$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 5 and number2 == 3 and number3 == 3:
        Balance += 10
        print("---------------")
        print("-[bar][🍒][🍒]-")
        print("---------------")
        print("--You won 10$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 3 and number2 == 5 and number3 == 5:
        Balance += 30
        print("---------------")
        print("-[🍒][bar][bar]-")
        print("---------------")
        print("--You won 30$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 5 and number2 == 5 and number3 == 3:
        Balance += 30
        print("---------------")
        print("-[bar][bar][🍒]-")
        print("---------------")
        print("--You won 30$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 5 and number2 == 3 and number3 == 5:
        Balance += 30
        print("---------------")
        print("-[bar][🍒][bar]-")
        print("---------------")
        print("--You won 30$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 3 and number2 == 3 and number3 == 4:
        Balance += 20
        print("---------------")
        print("-[🍒][🍒][🫐]-")
        print("---------------")
        print("--You won 20$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 3 and number2 == 4 and number3 == 3:
        Balance += 20
        print("---------------")
        print("-[🍒][🫐][🍒]-")
        print("---------------")
        print("--You won 20$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 4 and number2 == 3 and number3 == 3:
        Balance += 20
        print("---------------")
        print("-[🫐][🍒][🍒]-")
        print("---------------")
        print("--You won 20$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 3 and number2 == 4 and number3 == 4:
        Balance += 25
        print("---------------")
        print("-[🍒][🫐][🫐]-")
        print("---------------")
        print("--You won 25$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 4 and number2 == 4 and number3 == 3:
        Balance += 25
        print("---------------")
        print("-[🫐][🫐][🍒]-")
        print("---------------")
        print("--You won 25$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 4 and number2 == 3 and number3 == 4:
        Balance += 25
        print("---------------")
        print("-[🫐][🍒][🫐]-")
        print("---------------")
        print("--You won 25$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 6 and number2 == 5 and number3 == 4:
        Balance += 10
        print("---------------")
        print("-[7️⃣][bar][🫐]-")
        print("---------------")
        print("--You won 10$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 5 and number2 == 6 and number3 == 4:
        Balance += 10
        print("---------------")
        print("-[bar][7️⃣][🫐]-")
        print("---------------")
        print("--You won 10$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 5 and number2 == 4 and number3 == 6:
        Balance += 10
        print("---------------")
        print("-[bar][🫐][7️⃣]-")
        print("---------------")
        print("--You won 10$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 4 and number2 == 5 and number3 == 6:
        Balance += 10
        print("---------------")
        print("-[🫐][bar][7️⃣]-")
        print("---------------")
        print("--You won 10$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 3 and number2 == 4 and number3 == 5:
        Balance += 15
        print("---------------")
        print("-[🍒][🫐][bar]-")
        print("---------------")
        print("--You won 15$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 3 and number2 == 5 and number3 == 4:
        Balance += 15
        print("---------------")
        print("-[🍒][bar][🫐]-")
        print("---------------")
        print("--You won 15$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 4 and number2 == 3 and number3 == 5:
        Balance += 15
        print("---------------")
        print("-[🫐][🍒][bar]-")
        print("---------------")
        print("--You won 15$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 4 and number2 == 5 and number3 == 3:
        Balance += 15
        print("---------------")
        print("-[🫐][bar][🍒]-")
        print("---------------")
        print("--You won 15$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 5 and number2 == 3 and number3 == 4:
        Balance += 15
        print("---------------")
        print("-[bar][🍒][🫐]-")
        print("---------------")
        print("--You won 15$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 5 and number2 == 4 and number3 == 3:
        Balance += 15
        print("---------------")
        print("-[bar][🫐][🍒]-")
        print("---------------")
        print("--You won 15$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 4 and number2 == 6 and number3 == 5:
        Balance += 10
        print("---------------")
        print("-[🫐][7️⃣][bar]-")
        print("---------------")
        print("--You won 10$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 5 and number2 == 4 and number3 == 6:
        Balance += 10
        print("---------------")
        print("-[bar][🫐][7️⃣]-")
        print("---------------")
        print("--You won 10$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 5 and number2 == 6 and number3 == 4:
        Balance += 10
        print("---------------")
        print("-[bar][7️⃣][🫐]-")
        print("---------------")
        print("--You won 10$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 6 and number2 == 4 and number3 == 5:
        Balance += 10
        print("---------------")
        print("-[7️⃣][🫐][bar]-")
        print("---------------")
        print("--You won 10$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 6 and number2 == 5 and number3 == 4:
        Balance += 10
        print("---------------")
        print("-[7️⃣][bar][🫐]-")
        print("---------------")
        print("--You won 10$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 6 and number2 == 5 and number3 == 3:
        Balance += 5
        print("---------------")
        print("-[7️⃣][bar][🍒]-")
        print("---------------")
        print("--You won 5$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 3 and number2 == 5 and number3 == 6:
        Balance += 5
        print("---------------")
        print("-[🍒][bar][7️⃣]-")
        print("---------------")
        print("--You won 5$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 5 and number2 == 6 and number3 == 3:
        Balance += 5
        print("---------------")
        print("-[bar][7️⃣][🍒]-")
        print("---------------")
        print("--You won 5$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 3 and number2 == 4 and number3 == 6:
        Balance += 15
        print("---------------")
        print("-[🍒][🫐][7️⃣]-")
        print("---------------")
        print("--You won 15$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 3 and number2 == 6 and number3 == 4:
        Balance += 15
        print("---------------")
        print("-[🍒][7️⃣][🫐]-")
        print("---------------")
        print("--You won 15$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 6 and number2 == 4 and number3 == 3:
        Balance += 15
        print("---------------")
        print("-[7️⃣][🫐][🍒]-")
        print("---------------")
        print("--You won 15$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 6 and number2 == 3 and number3 == 4:
        Balance += 15
        print("---------------")
        print("-[7️⃣][🍒][🫐]-")
        print("---------------")
        print("--You won 15$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 4 and number2 == 6 and number3 == 3:
        Balance += 15
        print("---------------")
        print("-[🫐][7️⃣][🍒]-")
        print("---------------")
        print("--You won 15$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 4 and number2 == 3 and number3 == 6:
        Balance += 15
        print("---------------")
        print("-[🫐][🍒][7️⃣]-")
        print("---------------")
        print("--You won 15$--")
        print("---------------")
        print("-Balance: ", Balance)

    elif number1 == 6 and number2 == 3 and number3 == 5:
        Balance += 5
        print("---------------")
        print("-[7️⃣][🍒][bar]-")
        print("---------------")
        print("--You won 5$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 3 and number2 == 6 and number3 == 5:
        Balance += 5
        print("---------------")
        print("-[🍒][7️⃣][bar]-")
        print("---------------")
        print("--You won 5$--")
        print("---------------")
        print("-Balance: ", Balance)
    elif number1 == 5 and number2 == 3 and number3 == 6:
        Balance += 5
        print("---------------")
        print("-[bar][🍒][7️⃣]-")
        print("---------------")
        print("--You won 5$--")
        print("---------------")
        print("-Balance: ", Balance)


Balance = float(input("Enter your balance: "))


print("The Price of The Slots is 25$")
Price = 25
while True:

    if Price > Balance:
        print("Insufficient Funds...")
        break
    else:
        slots()

        response = input("Do you want to play again? (y/n): ")
        if response.lower() == "n":
            break  # exit the loop if user doesn't want to play again
        else:
            continue
print("Thanks for playing!")
