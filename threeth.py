import re

def normalize_phone(phone_number: str) -> str:
    # Удаляем все символы, кроме цифр и символа '+'
    clean_number = re.sub(r'[^\d+]', '', phone_number)

    # Если номер начинается с '+380', то он уже в международном формате
    if clean_number.startswith('+380'):
        return clean_number
    
    # Если номер начинается с '380', добавляем '+' в начало
    if clean_number.startswith('380'):
        return f'+{clean_number}'
    
    # Если номер начинается с '0', добавляем '+38' в начало
    if clean_number.startswith('0'):
        return f'+38{clean_number}'
    
    # Если номер уже начинается с '+', но не с '+380', возвращаем как есть
    if clean_number.startswith('+'):
        return clean_number
    
    # В остальных случаях добавляем '+38' в начало
    return f'+38{clean_number}'