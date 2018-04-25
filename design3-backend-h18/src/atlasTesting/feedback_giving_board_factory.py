from atlas.game.BoardFactory import VisionBoardFactory
from atlas.game.board import Board
from atlas.vision.gameboard_visualizer import board_to_image


class FeedbackGivingBoardFactory(VisionBoardFactory):

    def create_board(self) -> Board:
        board = super().create_board()
        board_to_image(board).show_and_close(timeout=1000)
        return board

