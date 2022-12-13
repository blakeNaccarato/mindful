"""Configure trellens."""

from pathlib import Path

from pydantic import BaseModel, DirectoryPath, Field
import tomllib

APPDIR = Path("~/.trellens").expanduser()


def init():
    """Initialize the application."""
    APPDIR.mkdir(exist_ok=True)
    generate_schema()


class AppConfig(BaseModel):
    """Application configuration."""

    boards: DirectoryPath = Field(
        ..., description="Directory containing exported Trello baords."
    )


def get_config():
    """Get default configuration."""
    config = APPDIR / "config.toml"
    return AppConfig(**tomllib.loads(config.read_text(encoding="utf-8")))


def generate_schema():
    """Write the configuration schema."""
    schema = APPDIR / "config-schema.json"
    schema.write_text(AppConfig.schema_json(indent=2) + "\n", encoding="utf-8")
