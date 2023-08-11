# Ruff SQLAlchemy Repro for TCH003

This repo is meant to reproduce an issue with TCH003 in ruff, in particular how it autofixes for SQLAlchemy.

Currently, the recommended autofix leads to an error with SQLAlchemy:

> sqlalchemy.exc.ArgumentError: Could not resolve all types within mapped annotation: "Mapped[date]".  Ensure all types are written correctly and are imported within the module in use.

## Steps to reproduce

- Install poetry 1.5.1, or create a virtualenv to pip install the documented versions in `pyproject.toml`
- `poetry install`
- `poetry run python main.py` -- note that this works appropriately
- `poetry run ruff src`
- `poetry run ruff --fix src`
- `poetry run python main.py` -- note that we get the aforementioned error.

## Discussion

This error is sqlalchemy-specific, but the autofix actually introduces bugs.

A current work-around is to disable TCH003.

One consideration is that SQLAlchemy models imported as part of a `Mapped[Model]` relationship will need to go under the `TYPE_CHECKING` flag, while std lib types are not supported in this fashion. The likely cause of this is that `Mapped["Model"]` is supported, while `Mapped["date"]` is not.
