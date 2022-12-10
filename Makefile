SOURCE_DIR=tests

run:
	poetry run pytest --headed

lint:
	isort $(SOURCE_DIR) \
	&& black $(SOURCE_DIR) \
	&& mypy $(SOURCE_DIR) \
	&& pylint -j 4 $(SOURCE_DIR)
