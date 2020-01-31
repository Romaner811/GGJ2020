import sys
from repairship.game.ball import BouncingBallApp


# TODO: split to different file.
class Size:
    def __init__(self, width, height):
        self.x = self.width = width
        self.y = self.height = height

    def get_pair(self):
        return self.x, self.y

    def __iter__(self):
        return iter(self.get_pair())


def main(args):
    app = BouncingBallApp(
        size=Size(800, 600),
        speed=Size(2, 2),
        bg=(0xFF, 0xFF, 0xFF)
    )

    errlvl = app.run()

    return errlvl


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
