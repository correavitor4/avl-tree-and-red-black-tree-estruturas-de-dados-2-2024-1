import random
import time

from alv_tree import AVLTree
from red_black_tree import RedBlackTree

tree = RedBlackTree()

generated_numbers: [int] = []
cont: int = 10000

while cont > 0:
    while True:
        random_number = random.randint(1, 1000000)
        if random_number not in generated_numbers:
            generated_numbers.append(random_number)
            tree.insert(random_number)
            cont -= 1
            break

# AVL tree
start_time = time.time()
tree = AVLTree()
for number in generated_numbers:
    tree.insertValue(number)
end_time = time.time()
elapsed_time = end_time - start_time
print("Árvore ALV: ")
print(f"Insersão completa: {elapsed_time} segundos")
print(f"Rotações: {tree.rotations}\n\n")

# Red black tree
start_time = time.time()
tree = RedBlackTree()
for number in generated_numbers:
    tree.insert(number)
end_time = time.time()
elapsed_time = end_time - start_time
print("Árvore REd black: ")
print(f"Insersão completa: {elapsed_time} segundos")
print(f"Rotações: {tree.rotations}")