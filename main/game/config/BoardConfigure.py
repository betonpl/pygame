from main.unit.Balanced import Balanced
from main.unit.Warrior import Warrior
from main.unit.Defender import Defender
from main.api.Player import Player
from main.api.Field import Field


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
        board.addField(Field(2, 0, Warrior(orangePlayer)))
        board.addField(Field(1, 1, Defender(orangePlayer)))
        board.addField(Field(0, 2, Balanced(orangePlayer)))
        board.addField(Field(2, 9, Warrior(orangePlayer)))
        board.addField(Field(1, 8, Defender(orangePlayer)))
        board.addField(Field(0, 7, Balanced(orangePlayer)))

        bluePlayer = Player("blue")
        board.addPlayer(bluePlayer)
        board.addField(Field(18, 9, Warrior(bluePlayer)))
        board.addField(Field(19, 8, Defender(bluePlayer)))
        board.addField(Field(20, 7, Balanced(bluePlayer)))
        board.addField(Field(18, 0, Warrior(bluePlayer)))
        board.addField(Field(19, 1, Defender(bluePlayer)))
        board.addField(Field(20, 2, Balanced(bluePlayer)))
