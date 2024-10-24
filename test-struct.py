import time
import tracemalloc
from random import uniform
import Struct

test_tree = Struct.Tree()

def generate_data(n,min_weight,max_weight):
    return [(i,uniform(min_weight,max_weight)) for i in range(1,n)]



def test_with_generate_date(n,m,min_weigh,max_weight):
    tracemalloc.start()
    start_time = time.time()
    for data in generate_data(m,min_weigh,max_weight):
        test_tree.add(*data)
    end_time = time.time()
    snapshot = tracemalloc.take_snapshot()
    print(snapshot.statistics('lineno')[0])
    tracemalloc.stop()
    print(f"Добавление {n} элементов:", end_time-start_time)
    start_time = time.time()
    for i in range(m):
        test_tree.get()
    end_time = time.time()
    print(f"Получение {m} элементов из дерева с {n} элементами:", end_time - start_time)


test_with_generate_date(1000,1000,0.001,10)