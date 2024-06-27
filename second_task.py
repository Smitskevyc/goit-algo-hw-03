# Импорт библиотек 
import random 

# Функция которая генерирует определенное количество уникальных билетов
def get_numbers_ticket(min: int, max: int, quantity: int) -> list:

    # Проверяем чтобі все условия были соблюдены
    if not (1 <= min <= max <= 1000) or not (1 <= quantity <= (max - min + 1)):
        return []

    # Генерируем уникальный список случайных номеров билетов 
    unique_tickets = random.sample(range(min, max + 1), quantity)

    #Cортируем список на месте    
    unique_tickets.sort()

    # Возвращяем список уникальных билетов
    return unique_tickets


# Примеры использования 

bad_use = get_numbers_ticket(0, 999, 4) 
print(bad_use) # Вывод [] - Пустой список т.к аргументы переданные в функцию были не корректны

good_use = get_numbers_ticket(1, 1000, 10)
print(good_use) # Вывод [108, 291, 398, 414, 514, 593, 673, 799, 869, 917] - Отсортированный список с уникальными значениями