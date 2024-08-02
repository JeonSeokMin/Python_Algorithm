def solution(edges):
    answer = [0, 0, 0, 0]
    node_out = {}
    node_in = {}
    visit_node = {}
    
    for a, b in edges:
        if a not in node_out:
            node_out[a] = []
        node_out[a].append(b)
        visit_node[a] = False
        visit_node[b] = False
        if b not in node_in:
            node_in[b] = []
        node_in[b].append(a)
        if b not in node_out:
            node_out[b] = []
    
    def find_generate(node_out, node_in):
        test = [[key, len(value)] for key, value in node_out.items()]
        test.sort(key=lambda x: x[1], reverse=True)
        for key, _ in test:
            if key not in node_in:
                return key
        return None
    
    def dfs(v, node_out, visit_node):
        node_in_graph = 0
        edge_in_graph = 0
        check = [v]
        
        while check:
            current = check.pop()
            if current in visit_node and not visit_node[current]:
                visit_node[current] = True
                node_in_graph += 1
                if current in node_out:
                    if node_out[current]:
                        edge_in_graph += 1
                    for i in node_out[current]:
                        if i in node_out and len(node_out[i]) > 1:
                            return 2
                        if i in visit_node and not visit_node[i]:
                            check.append(i)
        
        if node_in_graph == edge_in_graph:
            return 0  # 도넛
        else:
            return 1  # 막대
    
    turn = find_generate(node_out, node_in)
    if turn is not None:
        answer[0] = turn
        for i in node_out[turn]:
            answer_value = dfs(i, node_out, visit_node)
            if 0 <= answer_value < 3:
                answer[answer_value + 1] += 1
    
    return answer