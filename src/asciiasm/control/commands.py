"""Provide commands for the application."""

from asciiasm.files import load, save

class Command():
    """Commands to use app."""

    command_dict = {"load sprite": load.load_sprite, "save canvas": save.save_image}
    args: list[str]
    command: str

    def __init__(self, cmd_input: str) -> None:
        self.command_func = self.command_dict[" ".join((word_list := cmd_input.split(" "))[:2])]
        self.args = word_list[2:]
