from turtlebot.turtle import Turtle


class ParseError(Exception):
    pass


class TurtleLang:
    def __init__(self, turtle: Turtle):
        self.turtle = turtle

        self.functions = {
            "F": turtle.forward,
            "B": turtle.backwards,
            "L": turtle.left,
            "R": turtle.right,
            "P": turtle.set_pen,
            "A": turtle.set_angle,
        }

    def parse(self, script: str):
        steps = script.split(",")

        for i, _step in enumerate(steps):
            step = _step.strip()

            

            try:
                value = step[1:]
                func = step[0].upper()
                self.functions[func](int(value))
            except KeyError:
                raise ParseError(f"Unkown method: '{func}'")
            except (ValueError, IndexError):
                if value:
                    raise ParseError(
                        f"'{step[1:]}' is not a valid integer in step {i}: '{step}'."
                    )
                else:
                    raise ParseError(f"Missing value for step {i}: '{step}'")
