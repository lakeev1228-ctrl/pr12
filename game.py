import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("🎯 Добро пожаловать в игру 'Угадай число'!")
    print(f"Я загадал число от 1 до 100. У тебя {max_attempts} попыток!")
    
    while attempts < max_attempts:
        try:
            guess = int(input("➡️  Введи свою догадку: "))
            attempts += 1
            
            if guess < number:
                print("📈 Загаданное число БОЛЬШЕ")
            elif guess > number:
                print("📉 Загаданное число МЕНЬШЕ")
            else:
                print(f"🎉 Поздравляю! Ты угадал число {number} за {attempts} попыток!")
                return
        
        except ValueError:
            print("❌ Пожалуйста, введи целое число!")
    
    print(f"💔 К сожалению, попытки закончились. Загаданное число было: {number}")

if __name__ == "__main__":
    guess_number()