echo off
@echo.
@echo === pytest  ===
uv run coverage run -m pytest
@echo.
@echo === Coverage text  ===
uv run coverage report -m
@echo.
@echo === Coverage html  ===
uv run coverage html
@echo.
