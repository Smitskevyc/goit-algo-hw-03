# Импорт библиотек
from datetime import datetime as dt

# Функция которая принимает дату в формате "YYYY-MM-DD" и возвращяет разницу от нынешнего времени.
def get_days_from_today(date: str) -> int:
    
    # Преобразуем строковое значение даты в объект datetime
    data_time_obj = dt.strptime(date, "%Y-%m-%d")
    # Получаем дату на данный момент
    data_time_now = dt.today()
    # Получаем разницу во времени 
    data_difference = int(data_time_obj - data_time_now)

    # Возвращяем разницу применим свойство объекта days
    return data_difference.days

# Пример для использования  
print(get_days_from_today("2024-03-11")) # Вывод : -109