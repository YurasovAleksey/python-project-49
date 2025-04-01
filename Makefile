install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

reinstall-package:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check brain_games

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc
