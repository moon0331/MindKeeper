from src.package.graph import MindGraph

if __name__ =='__main__':
    g = MindGraph()
    #g.add_edge_from_line("1 3 5 2 1 17 50")
    g.add_edge_from_line(input())
    g.draw(True, 1)
    g.get_shortest_path('1','2')
    print(g.show_weight_info())
    print('end')