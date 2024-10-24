from random import choices

# не работает удаление и изменение весов
# добавляется и получается элемент за log(n)   (вроде бы)

class Node:
    def __init__(self):
        self.counter = 0
        self.x = 0
        self.weight = 0


class Tree:
    def __init__(self):
        self.nodes = [None,Node()]

    def update_node(self,i,x,weight):
        self.nodes[i].x = x
        self.nodes[i].weight = weight

    def rand_chose(self, iterts):
        weights = [self.nodes[i].weight  for i in iterts]
        weights[0] -= self.nodes[2*iterts[0]].weight + self.nodes[2*iterts[0]+1].weight
        return choices(iterts,weights=weights)[0]


    def add(self,x,weight):
        i = 1
        while self.nodes[i].counter > 1:
            self.nodes[i].weight += weight
            self.nodes[i].counter += 1
            if self.nodes[i*2].counter <= self.nodes[i*2+1].counter:
                i = i*2
            else:
                i = i*2+1
        if self.nodes[i].x == 0:
            self.nodes[i].weight += weight
            self.nodes[i].x = x
            return
        if 4 * i + 2 > len(self.nodes):
            self.nodes += [Node() for i in range(len(self.nodes))]
        self.nodes[i].weight += weight
        if self.nodes[i].counter == 1:
            self.update_node(i * 2+1,x,weight)
        else:
            self.update_node(i * 2,x,weight)
        self.nodes[i].counter += 1

    def get(self):
        i = 1
        while self.nodes[i].counter:
            can = [i,2*i,2*i+1]
            new_i = self.rand_chose(can)
            if new_i == i:
                return self.nodes[i].x
            i = new_i
        return self.nodes[i].x

