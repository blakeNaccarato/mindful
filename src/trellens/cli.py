"""CLI for Lens for Trello."""

from datetime import UTC, date, datetime, time, timedelta
from pathlib import Path

from datamodel_code_generator import InputFileType, PythonVersion, generate
import pyperclip
from typer import Typer

from trellens.defaults import boards

app = Typer()


@app.command()
def get_comments(
    board_name: str,
    card_name: str,
    limit_days: int = 0,
):
    """Get comments from a card."""
    board = [board for board in boards if board.name == board_name][0]
    comment_actions_data = [
        action for action in board.actions if action.type == "commentCard"
    ]
    today = datetime.combine(date.today(), time.min).astimezone(UTC)
    date_limit = today - timedelta(days=limit_days) if limit_days != 0 else None
    filtered_comments = reversed(
        [
            action.data.text
            for action in comment_actions_data
            if action.data.text
            and action.data.card
            and action.data.card.name
            and action.data.card.name == card_name
            and (not date_limit or datetime.fromisoformat(action.date) > date_limit)
        ]
    )
    pyperclip.copy("\n\n\n".join(filtered_comments))


# * -------------------------------------------------------------------------------- * #
# * BACKEND


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
