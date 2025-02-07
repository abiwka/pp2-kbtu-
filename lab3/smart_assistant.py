import random
from function1 import  fahrenheit_to_celsius, filter_prime, reverse_sentence

def guess_the_number():
    print("\n🎮 'Жасырын нөмірді тап!' ойынына қош келдіңіз!")
    name = input("Атыңызды енгізіңіз: ")
    number = random.randint(1, 20)
    attempts = 0
    
    print(f"Жарайсың, {name}! Мен 1 мен 20 арасындағы бір санды жасырдым. Таба аласың ба?")
    
    while True:
        guess = int(input("Болжам жаса: "))
        attempts += 1
        if guess < number:
            print("📉 Өте кіші! Тағы бір рет көріңіз.")
        elif guess > number:
            print("📈 Өте үлкен! Қайта көріңіз.")
        else:
            print(f"🎉 Құттықтаймын, {name}! Сіз {attempts} әрекетте санды таптыңыз!")
            break

def main():
    print("🤖 Қош келдіңіз! Бұл – сіздің ақылды көмекшіңіз.")
    while True:
        print("\n🔹 Мен не істей аламын?")
        print(" 1 Фаренгейттен Цельсийге ауыстыру")
        print(" 2 Жай сандарды сүзу")
        print(" 3 Сөйлемді кері қайтару")
        print(" 4 'Жасырын нөмірді тап!' ойынын ойнау")
        print(" 0️ Шығу")
        
        choice = input("Өзіңізге қажетті нөмірді таңдаңыз: ")

        if choice == "1":
            fahrenheit = float(input("Фаренгейт градусын енгізіңіз: "))
            print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit)}°C.")
        
        
        elif choice == "2":
            numbers = list(map(int, input("Бос орынмен бөлінген сандар тізімін енгізіңіз: ").split()))
            print("Жай сандар:", filter_prime(numbers))
        
        elif choice == "3":
            sentence = input("Сөйлем енгізіңіз: ")
            print("Кері ретімен жазылған сөйлем:", reverse_sentence(sentence))
        
        elif choice == "4":
            guess_the_number()
        
        elif choice == "0":
            print("👋 Бағдарлама аяқталды! Келесі кездескенше!")
            break
        
        else:
            print("⚠ Қате! Дұрыс нөмірді таңдаңыз.")

if __name__ == "__main__":
    main()
