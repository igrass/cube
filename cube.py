#!/usr/bin/env python2
import os
import sys
import time

import copy


class Cube():

    def __init__(self):
        self.cubeSize = 5
        self.cubeColor = range(1, 7)

    def initCube(self):
        # cubeMatrix = [x][y][x][3] stand for the color of the side. 3 sides: 0 xy, 1 xz, 2 yz
        self.cubeMatrix = [[[[0 for side in range(3)] for z in range(self.cubeSize + 1)] for y in range(self.cubeSize + 1)] for x in range(self.cubeSize + 1)]

        for i in range(self.cubeSize):
            for j in range(self.cubeSize):
                self.cubeMatrix[i][j][0][0] = self.cubeColor[0]
                self.cubeMatrix[i][0][j][1] = self.cubeColor[1]
                self.cubeMatrix[0][i][j][2] = self.cubeColor[2]
                self.cubeMatrix[i][j][self.cubeSize][0] = self.cubeColor[3]
                self.cubeMatrix[i][self.cubeSize][j][1] = self.cubeColor[4]
                self.cubeMatrix[self.cubeSize][i][j][2] = self.cubeColor[5]

    def moveCube(self, side, layer, turn):
        # side: 0 xy, 1 xz, 2 yz
        # layer: range(cubeSize)
        # turn: range(1, 4)

        for trunTime in range(turn):
            if side == 0:
                # side xy
                cubeMatrixCopy = copy.deepcopy(self.cubeMatrix)
                for i in range(self.cubeSize):
                    for j in range(self.cubeSize):
                        cubeMatrixCopy[self.cubeSize - 1 - j][i][layer][0] = self.cubeMatrix[i][j][layer][0]
                        cubeMatrixCopy[self.cubeSize - 1 - j][i][layer + 1][0] = self.cubeMatrix[i][j][layer + 1][0]
                for i in range(self.cubeSize + 1):
                    for j in range(self.cubeSize + 1):
                        cubeMatrixCopy[i][j][layer][1] = cubeMatrixCopy[i][j][layer][2] = 0
                for i in range(self.cubeSize):
                    cubeMatrixCopy[self.cubeSize][i][layer][2] = self.cubeMatrix[i][0][layer][1]
                    cubeMatrixCopy[self.cubeSize - 1 - i][self.cubeSize][layer][1] = self.cubeMatrix[self.cubeSize][i][layer][2]
                    cubeMatrixCopy[0][self.cubeSize - 1 - i][layer][2] = self.cubeMatrix[self.cubeSize - 1 - i][self.cubeSize][layer][1]
                    cubeMatrixCopy[i][0][layer][1] = self.cubeMatrix[0][self.cubeSize - 1 - i][layer][2]

                self.cubeMatrix = cubeMatrixCopy

            elif side == 1:
                # side xz
                cubeMatrixCopy = copy.deepcopy(self.cubeMatrix)
                for i in range(self.cubeSize):
                    for j in range(self.cubeSize):
                        cubeMatrixCopy[self.cubeSize - 1 - j][layer][i][1] = self.cubeMatrix[i][layer][j][1]
                        cubeMatrixCopy[self.cubeSize - 1 - j][layer + 1][i][1] = self.cubeMatrix[i][layer + 1][j][1]
                for i in range(self.cubeSize + 1):
                    for j in range(self.cubeSize + 1):
                        cubeMatrixCopy[i][layer][j][0] = cubeMatrixCopy[i][layer][j][2] = 0
                for i in range(self.cubeSize):
                    cubeMatrixCopy[self.cubeSize][layer][i][2] = self.cubeMatrix[i][layer][0][0]
                    cubeMatrixCopy[self.cubeSize - 1 - i][layer][self.cubeSize][0] = self.cubeMatrix[self.cubeSize][layer][i][2]
                    cubeMatrixCopy[0][layer][self.cubeSize - 1 - i][2] = self.cubeMatrix[self.cubeSize - 1 - i][layer][self.cubeSize][0]
                    cubeMatrixCopy[i][layer][0][0] = self.cubeMatrix[0][layer][self.cubeSize - 1 - i][2]

                self.cubeMatrix = cubeMatrixCopy[:]

            elif side == 2:
                # side yz
                cubeMatrixCopy = copy.deepcopy(self.cubeMatrix)
                for i in range(self.cubeSize):
                    for j in range(self.cubeSize):
                        cubeMatrixCopy[layer][self.cubeSize - 1 - j][i][2] = self.cubeMatrix[layer][i][j][2]
                        cubeMatrixCopy[layer + 1][self.cubeSize - 1 - j][i][2] = self.cubeMatrix[layer + 1][i][j][2]
                for i in range(self.cubeSize + 1):
                    for j in range(self.cubeSize + 1):
                        cubeMatrixCopy[layer][i][j][0] = cubeMatrixCopy[layer][i][j][1] = 0
                for i in range(self.cubeSize):
                    cubeMatrixCopy[layer][self.cubeSize][i][1] = self.cubeMatrix[layer][i][0][0]
                    cubeMatrixCopy[layer][self.cubeSize - 1 - i][self.cubeSize][0] = self.cubeMatrix[layer][self.cubeSize][i][1]
                    cubeMatrixCopy[layer][0][self.cubeSize - 1 - i][1] = self.cubeMatrix[layer][self.cubeSize - 1 - i][self.cubeSize][0]
                    cubeMatrixCopy[layer][i][0][0] = self.cubeMatrix[layer][0][self.cubeSize - 1 - i][1]

                self.cubeMatrix = cubeMatrixCopy[:]

    def printCube(self, side, layer):
        # side: 0 xy, 1 xz, 2 yz
        # layer: range(cubeSize)

        if side == 0:
            # side xy
            for i in range(self.cubeSize):
                for j in range(self.cubeSize):
                    print self.cubeMatrix[i][j][layer][0],
                print

        elif side == 1:
            # side xz
            for i in range(self.cubeSize):
                for j in range(self.cubeSize):
                    print self.cubeMatrix[i][layer][j][1],
                print

        elif side == 2:
            # side yz
            for i in range(self.cubeSize):
                for j in range(self.cubeSize):
                    print self.cubeMatrix[layer][i][j][2],
                print

        print


def main():
    cube = Cube()
    cube.initCube()
    print "start:"
    cube.printCube(0, 0)
    cube.printCube(1, 0)
    cube.printCube(2, 0)
    cube.printCube(0, cube.cubeSize)
    cube.printCube(1, cube.cubeSize)
    cube.printCube(2, cube.cubeSize)
    print "move:"
    cube.moveCube(0, 0, 1)
    cube.printCube(2, 0)
    print "move:"
    cube.moveCube(0, 2, 1)
    cube.printCube(2, 0)
    print "move:"
    cube.moveCube(1, 0, 1)
    cube.printCube(2, 0)
    print "move:"
    cube.moveCube(0, 0, 1)
    cube.printCube(2, 0)
    print "move:"
    cube.moveCube(0, 0, 1)
    cube.printCube(2, 0)


if __name__ == '__main__':
    main()
