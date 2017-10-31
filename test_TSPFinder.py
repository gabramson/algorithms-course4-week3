import TSPFinder

def test_TSPMaker():
    tsp_finder = TSPFinder.TSPFinder(6)
    tsp_finder.add_edge(1, 2, 1)
    tsp_finder.add_edge(2, 4, 0)
    tsp_finder.add_edge(3, 2, 0)
    tsp_finder.add_edge(4, 0, 0)
    tsp_finder.add_edge(5, 4, 3)
    tsp_finder.add_edge(6, 0, 3)
    assert tsp_finder.get_shortest_tour() == 15
