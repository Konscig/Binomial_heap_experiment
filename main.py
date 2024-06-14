import time
import random
from binomial_heap import BinomialHeap
from  heap import Heap

# Функция для симуляции добавления и обработки заказов в биномиальной куче
def simulate_binomial_heap_processing(num_orders):
    heap = BinomialHeap()
    start_time_add = time.time()
    for i in range(num_orders):
        timestamp = random.randint(0, 1000)  # Симуляция заказов с одинаковыми временными метками
        heap.insert((timestamp, i))
    end_time_add = time.time()

    start_time_process = time.time()
    while not heap.is_empty():
        heap.delete_min()
    end_time_process = time.time()

    time_add = (end_time_add - start_time_add) * 1000  # в миллисекундах
    time_process = (end_time_process - start_time_process) * 1000  # в миллисекундах

    return time_add, time_process

# Количество заказов для эксперимента
order_counts = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 500000, 1000000]

# Инициализация списка результатов
results = []

# Запуск симуляции для разного количества заказов
for count in order_counts:
    time_add, time_process = simulate_binomial_heap_processing(count)
    results.append((count, time_add, time_process))

# Печать результатов в табличном формате
print(f"{'Количество заказов':<20}{'Время добавления (мс)':<25}{'Время обработки (мс)':<25}")
for count, time_add, time_process in results.copy():
    print(f"{count:<20}{time_add:<25.2f}{time_process:<25.2f}")
