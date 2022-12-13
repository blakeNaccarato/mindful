import json
from pathlib import Path

from trellens.board import Model


def load_boards(path: Path) -> list[Model]:
    """Load Trello boards."""
    return [load_board(path) for path in path.glob("*.json")]


def load_board(path: Path) -> Model:
    """Load a Trello board."""
    return Model(**json.loads(path.read_text(encoding="utf-8")))
