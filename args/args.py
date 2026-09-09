"""

minimalistic tool to see if correct arguments are passed to the program or not

"""


class Args:
    def __init__(self, nb_args: int, usage: str, args: list):
        self.nb_args: int = nb_args
        self.usage: str = usage
        self.args: list[str] = args

    def is_valid(self) -> str | None:
        if len(self.args) != self.nb_args:
            return self.usage
        return None
