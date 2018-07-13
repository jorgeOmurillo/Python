from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

def arbol(lista):
    plista = lista.split()
    eTree = BinaryTree('')
    stacked = Stack()
    stacked.push(eTree)
    current = eTree

    for i in plista:
        if i == '(':
            current.insertLeft('')
            stacked.push(current)
            current = current.getLeftChild()
        elif i not in ['+','-','/','*', ')']:
            current.key = int(i)
            parent = stacked.pop()
            current = parent
        elif i in ['+','-','/','*']:
            current.key = i
            stacked.push(current)
            current.insertRight('')
            current = current.getRightChild()
        elif i == ')':
            current = stacked.pop()
        else:
            raise ValueError

    return eTree


test = arbol("( ( 10 + 5 ) * 3 )")
test.postorder()

import operator

def evaluate(parseTree):
    op = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    left = parseTree.getLeftChild()
    right = parseTree.getRightChild()

    if left and right:
        fn = op[parseTree.getRootVal()]
        return fn(evaluate(left), evaluate(right))
    else:
        return parseTree.getRootVal()

print('Tree result -> ', evaluate(test))
