"""Defaults for trellens."""

from trellens.api import load_boards
from trellens.config import get_config

config = get_config()
boards = load_boards(config.boards)
