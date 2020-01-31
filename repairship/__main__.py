import sys
from repairship.game.astronaut import AstronautApp
from repairship.core.sizes import Size


def main(args):
    app = AstronautApp(
        size=Size(800, 600),
        fps=60  # DEBUG
    )

    errlvl = app.run()

    return errlvl


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
