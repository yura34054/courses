def main():

    n = int(input())

    node_children = {}
    node_h = {i: 1 for i in range(n)}
    node_parent = []

    for node, parent in enumerate(map(int, input().split())):
        if parent == -1:
            root = node
            node_parent.append(-1)
            continue

        if parent in node_children: node_children[parent].append(node)
        else: node_children[parent] = [node]

        node_parent.append(parent)


    current_level = list(set(range(n)).difference(set(node_children.keys())))
    next_level = set()

    while len(current_level) > 1 or current_level[0] != root:
        for node in current_level:
            if node == root:
                next_level.add(root)
                continue

            if node_h[node_parent[node]] < node_h[node] + 1:
                next_level.add(node_parent[node])
                node_h[node_parent[node]] = node_h[node] + 1

        current_level, next_level = list(next_level), set()
    
    print(node_h[root])

    
    
main()