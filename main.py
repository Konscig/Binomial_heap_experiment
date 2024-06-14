import time
import random
from binomial_heap import BinomialHeap, Node
from datetime import datetime
from tabulate import tabulate

# Ваш класс BinomialHeap и код, связанный с ним, остаются такими же

def run_experiment(k_values, n_values):
    results = []

    for k in k_values:
        for n in n_values:
            heaps = [BinomialHeap() for _ in range(k)]
            orders = [int(time.mktime(datetime.now().timetuple())) + random.randint(1, 1000) for _ in range(n)]

            # Вставляем элементы в каждую кучу
            for i in range(k):
                if i < n:
                    heaps[i].insert(orders[i])

            start_time = time.time()
            for i in range(n):
                heaps[i % k].insert(orders[i])
            fill_duration = (time.time() - start_time) * 1000

            start_time = time.time()
            main_heap = BinomialHeap()
            for heap in heaps:
                main_heap.merge_heaps(heap)
            merge_duration = (time.time() - start_time) * 1000

            start_time = time.time()
            while main_heap.size > 0:  # Проверяем, что куча не пуста перед извлечением
                main_heap.delete_min()
            extract_duration = (time.time() - start_time) * 1000

            results.append([k, n, f"{fill_duration:.2f} ms", f"{merge_duration:.2f} ms", f"{extract_duration:.2f} ms"])

    headers = ["k", "n", "Fill Duration", "Merge Duration", "Extract Duration"]
    print(tabulate(results, headers=headers, tablefmt="grid"))

k_values = [5, 10, 15]
n_values = [100, 1000, 10000]

run_experiment(k_values, n_values)