from main.Field import Field
from main.impl.Player import Player
from main.unit.Balanced import Balanced


class BoardConfigure(object):

    def __init__(self, board):
        self.__board = board
        self.init()

    @property
    def board(self):
        return self.__board

    def init(self):
        board = self.board
        orangePlayer = Player("orange")
        board.addPlayer(orangePlayer)
        board.addField(Field(0, 0, Balanced(orangePlayer)))
        board.addField(Field(1, 0, Balanced(orangePlayer)))
