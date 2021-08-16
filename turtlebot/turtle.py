import io
import math
from typing import Tuple

from PIL import Image, ImageDraw


class Turtle:
    def __init__(self, size_x: int, size_y: int, bg: Tuple[int]):

        self._image = Image.new("RGB", (size_x, size_y), bg)
        self._cv = ImageDraw.Draw(self._image)

        self._pos = (size_x//2, size_y//2)
        self._angle = 0

        self._pen_down = True

    def left(self, degrees: int):
        """
        Turn the turtle left
        """
        self._angle -= degrees

    def right(self, degrees: int):
        """
        Turn the turtle right
        """
        self._angle += degrees

    def set_angle(self, degrees: int):
        """
        Set the turtles rotation
        """
        self._angle = degrees

    def pen_down(self):
        """
        Stop making lines
        """
        self._pen_down = True

    def pen_up(self):
        """
        Start making lines
        """
        self._pen_down = False

    def set_pen(self, state: bool):
        """
        Set the pen to be up or down
        """
        self._pen_down = bool(state)

    def _move(self, pixels: int):
        """
        Move the turtle a certain number of pixels in the direction the turtle
        is facing
        """

        change_x = round(math.cos(math.radians(self._angle)), 2) * pixels

        change_y = round(math.sin(math.radians(self._angle)), 2) * pixels

        new_x = self._pos[0] + change_x
        new_y = self._pos[1] + change_y

        if self._pen_down:
            self._cv.line(
                (
                    *self._pos,
                    new_x,
                    new_y,
                ),
                fill=0,
            )

        self._pos = (new_x, new_y)

    def forward(self, pixels: int):
        """
        Move the turtle forward
        """
        self._move(pixels)

    def backwards(self, pixels: int):
        """
        Move the turtle backwards
        """
        self._move(-pixels)

    def save_as_bytes(self) -> io.BytesIO:
        """
        Save the drawn image as a io.BytesIO() object
        """
        image_binary = io.BytesIO()
        self._image.save(image_binary, "PNG")
        image_binary.seek(0)
        return image_binary

    def save(self, filename: str):
        """
        Save the drawn image into a file
        """
        self._image.save(filename)
