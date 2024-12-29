import time
import tracemalloc
from random import uniform
import Struct
import Struct2

test_tree = Struct.Tree()
test_tree_2 = Struct2.RedBlackTree()
def generate_data(n,min_weight,max_weight):
    return [(i,uniform(min_weight,max_weight)) for i in range(1,n)]



def test_with_generate_date(test_struct,n,m,min_weigh,max_weight):
    tracemalloc.start()
    g_data = generate_data(n,min_weigh,max_weight)
    start_time = time.time()
    for data in g_data:
        test_struct.add(*data)
    end_time = time.time()
    snapshot = tracemalloc.take_snapshot()
    print(snapshot.statistics('lineno')[0])
    tracemalloc.stop()
    print(f"Добавление {n} элементов:", end_time-start_time)

    start_time = time.time()
    for i in range(m):
        test_struct.get()
    end_time = time.time()
    print(f"Получение {m} элементов из дерева с {n} элементами:", end_time - start_time)

    start_time = time.time()
    for i in range(m):
        test_struct.delete(i+1)
    end_time = time.time()
    print(f"Удаление {m} элементов из дерева с {n} элементами:", end_time - start_time)

def static_test(weights,struct,n):
    results = [0] * len(weights)
    t = len(weights)*10**n
    for _ in range(t):
        key = struct.get()
        results[key] += 1
    total_weight = struct.root.total_weight
    deviation = 0
    for i in range(1, 101):
        deviation += abs(results[i]-(weights[i]/total_weight)*t)
    deviation = deviation*100/t
    print(f"Отклонение: {deviation:.2f}% после {t} операций get")

def test_with_static_date():
    #test1
    test_struct = Struct2.RedBlackTree()
    weights = [0] 
    for i in range(1, 101):
        test_struct.add(i, i)
        weights.append(i)
    print("Test1")
    for i in range(1,4):static_test(weights,test_struct,i)

    #test2
    test_struct_2 = Struct2.RedBlackTree()
    weights_2 = [0] 
    for i in range(1, 101):
        test_struct_2.add(i, i)
        if i % 2:
            test_struct_2.delete(i)
            weights_2.append(0)
        else:weights_2.append(i)
    print("Test2")
    for i in range(1,4):static_test(weights_2,test_struct_2,i)

    #test3
    test_struct_3 = Struct2.RedBlackTree()
    weights_3 = [0] 
    for i in range(1, 101):
        test_struct_3.add(i, i)
        test_struct_3.add(i,2*i)
        weights_3.append(2*i)
    print("Test3")
    for i in range(1,4):static_test(weights_3,test_struct_3,i)

    #test4
    test_struct_4 = Struct2.RedBlackTree()
    weights_4 = [0] 
    for i in range(1, 101):
        test_struct_4.add(i, i)
        test_struct_4.add(i,2*i)
        if i % 2:
            test_struct_4.delete(i)
            weights_4.append(0)
        else:weights_4.append(2*i)
    print("Test4")
    for i in range(1,4):static_test(weights_4,test_struct_4,i)

    
print("Struct_2")
test_with_generate_date(test_tree_2,10000,10000,0.001,10)
test_with_generate_date(test_tree_2,100000,1000000,0.001,10)
test_with_generate_date(test_tree_2,1000000,1000000,0.001,10)
test_with_static_date()