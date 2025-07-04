import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    node_colors = [colors.get(node, 'skyblue') for node in tree.nodes()]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()


def build_heap_tree(heap, index=0):
    #TODO Реалізація функції побудови дерева бінарної купи (Взяти з попереднього завдання)
    if index >= len(heap):
        return None
    node = Node(heap[index])
    node.left = build_heap_tree(heap, 2 * index + 1)
    node.right = build_heap_tree(heap, 2 * index + 2)
    return node


def generate_color(step, total_steps):
    base_color = [135, 206, 250]
    #TODO Додати обрахунок відтінку кольору відповідно до послідовності його проходження
    end_color = [220, 235, 255]

    def interpolate(start, end, darken_factor):
        return int(start + (end - start) * darken_factor)

    darken_factor = step / max(total_steps - 1, 1)

    new_color = [interpolate(base_color[i], end_color[i], darken_factor) for i in range(3)]

    return f'#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}'


def dfs_visualize(root, total_steps):
    visited = set()
    stack = [root]
    colors = {}
    step = 0

    #TODO Реалізація алгоритму DFS
    while stack:
        node = stack.pop()
        if node and node.id not in visited:
            visited.add(node.id)
            colors[node.id] = generate_color(step, total_steps)
            step += 1

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return colors


def bfs_visualize(root, total_steps):
    visited = set()
    queue = [root]
    colors = {}
    step = 0

    #TODO Реалізація алгоритму BFS
    while queue:
        node = queue.pop(0)
        if node and node.id not in visited:
            visited.add(node.id)
            colors[node.id] = generate_color(step, total_steps)
            step += 1

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return colors


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


if __name__ == '__main__':
    heap_list = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]
    heapq.heapify(heap_list)
    heap_tree_root = build_heap_tree(heap_list)

    total_steps = count_nodes(heap_tree_root)

    dfs_colors = dfs_visualize(heap_tree_root, total_steps)
    draw_tree(heap_tree_root, dfs_colors)

    bfs_colors = bfs_visualize(heap_tree_root, total_steps)
    draw_tree(heap_tree_root, bfs_colors)
