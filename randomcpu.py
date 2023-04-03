import random
import concurrent.futures

# Функция для перемешивания строк
def shuffle_lines(lines):
    random.shuffle(lines)
    return lines

# Открываем файл для чтения
with open('File.txt', 'r') as f:
    # Читаем все строки в список
    lines = f.readlines()

# Разбиваем список на части по количеству потоков
threads = 10
chunksize = len(lines) // threads
chunks = [lines[i:i+chunksize] for i in range(0, len(lines), chunksize)]

# Создаем пул потоков
with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
    # Запускаем перемешивание строк в каждом чанке
    futures = [executor.submit(shuffle_lines, chunk) for chunk in chunks]

    # Собираем перемешанные строки из результатов выполнения потоков
    result = []
    for future in concurrent.futures.as_completed(futures):
        result.extend(future.result())

# Открываем файл для записи
with open('OutRandom.txt', 'w') as f:
    # Записываем перемешанные строки
    f.writelines(result)