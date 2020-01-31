import sys
from repairship.game.ball import BouncingBallApp
from repairship.core.sizes import Size


def main(args):
    app = BouncingBallApp(
        size=Size(800, 600),
        speed=Size(2, 2),
        bg=(0xFF, 0xFF, 0xFF),
        fps=10  # DEBUG
    )

    errlvl = app.run()

    return errlvl


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
