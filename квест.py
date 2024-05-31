import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    guess = None
    attempts = 0

    while guess != number_to_guess:
        guess = int(input("Вгадайте число від 1 до 10: "))
        attempts += 1
        if guess < number_to_guess:
            print("Занадто маленьке число. Спробуй ще раз.")
        elif guess > number_to_guess:
            print("Занадто велике число. Спробуй ще раз.")

    print(f"Вітаю! Ви вгадали число {number_to_guess} за {attempts} спроб.")

guess_the_number()