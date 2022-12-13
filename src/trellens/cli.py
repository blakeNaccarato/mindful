"""CLI for Lens for Trello."""

from pathlib import Path

from datamodel_code_generator import InputFileType, PythonVersion, generate
import pyperclip
from typer import Typer

from trellens.api import load_boards

app = Typer()


@app.command()
def generate_model(input_file: Path, output_file: Path):
    """Generate data model from JSON file."""
    generate(
        input_file,
        output=output_file,
        input_file_type=InputFileType.Json,
        snake_case_field=True,
        target_python_version=PythonVersion.PY_311,
    )


@app.command()
def get_comments(boards: Path, board_name: str, card_name: str):
    """Get comments from a card."""
    board = [board for board in load_boards(boards) if board.name == board_name][0]
    comment_actions_data = [
        action.data for action in board.actions if action.type == "commentCard"
    ]
    comment_actions_filtered = [
        data.text
        for data in comment_actions_data
        if data.text and data.card and data.card.name and data.card.name == card_name
    ]
    pyperclip.copy("\n\n".join(comment_actions_filtered))
