#!/usr/bin/env python3
"""
Module Docstring
"""
import TSPFinder

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    myfile = open("nn.txt", "r")
    vertices = int(myfile.readline())
    tsp_finder = TSPFinder.TSPFinder(vertices)
    for line in myfile:
        values = line.split()
        tsp_finder.add_edge(int(values[0]), float(values[1]), float(values[2]))
    print(tsp_finder.get_shortest_tour())

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
