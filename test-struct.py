import time
import tracemalloc
from random import uniform
import Struct
import Struct2

test_tree = Struct.Tree()
test_tree_2 = Struct2.RedBlackTree()
def generate_data(n,min_weight,max_weight):
    return [(i,uniform(min_weight,max_weight)) for i in range(1,n)]



def test_with_generate_date(test,n,m,min_weigh,max_weight):
    tracemalloc.start()
    start_time = time.time()
    for data in generate_data(n,min_weigh,max_weight):
        test.add(*data)
    end_time = time.time()
    snapshot = tracemalloc.take_snapshot()
    print(snapshot.statistics('lineno')[0])
    tracemalloc.stop()
    print(f"Добавление {n} элементов:", end_time-start_time)
    start_time = time.time()
    for i in range(m):
        test.get()
    end_time = time.time()
    print(f"Получение {m} элементов из дерева с {n} элементами:", end_time - start_time)


print("Просто дерево")
test_with_generate_date(test_tree,100000,1000,0.001,10)
print("Красно-чёрное дерево")
test_with_generate_date(test_tree_2,100000,100000,0.001,10)