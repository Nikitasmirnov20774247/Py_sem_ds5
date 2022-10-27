# Задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.

def word_delete(word):
    return False if 'абв' in word else True

def print_result():
    word = input('Введите текст через пробел: \n')
    word = word.split()
    print('Результат формирования списка:')
    print(word)
    print('Результат фильтрации (удалени слов с одержанием "абв") списка:')
    result = list(filter(word_delete,word))
    print(result)

print_result()