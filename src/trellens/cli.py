"""CLI for Lens for Trello."""

from pathlib import Path

from datamodel_code_generator import InputFileType, PythonVersion, generate
from typer import Typer

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
