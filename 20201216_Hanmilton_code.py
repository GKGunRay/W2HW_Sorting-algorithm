# 20201216
# This code is from here: https://stackoverflow.com/questions/47982604/hamiltonian-path-using-python
# pt->node

# def hamilton({節點編號:[相連接節點], ...}, 指定行經多少條路徑, 當前位置節點（初次輸入的值即起始位置）, 已經過路徑):
def hamilton(G, size, node, path=[]):
    print('Hamilton called with node={}, path={}'.format(node, path))
    if node not in set(path):
        path.append(node)
        if len(path)==size:
            return path
        for node_next in G.get(node, []):
            res_path = [i for i in path]
            candidate = hamilton(G, size, node_next, res_path)
            if candidate is not None:  # skip loop or dead end | 無限迴圈或死路跳過
                return candidate
        print('path {} is a dead end'.format(path)) # 此路徑是死路（結束），上方未結束的recursion繼續。
    else:
        print('node {} already in path {}'.format(node, path))
    # loop or dead end, none is implicitly returned
    # 直接輸出，不return。

print("Examples:\n"+"-"*30)
G = {1:[2,3,4], 2:[1,3,4], 3:[1,2,4], 4:[1,2,3]}
hamilton(G, 4, 1)
print("-"*30)
G = {1:[2], 2:[3,4], 4:[3]}
hamilton(G, 4, 1)
print("-"*30)
G = {1:[2], 2:[3,4], 4:[3]}
hamilton(G, 4, 2)
