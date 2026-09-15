import customtkinter as ctk
import pytest

from gui import Gui


@pytest.fixture
def app():
    app = Gui()
    yield app
    app.destroy()


def test_divisors_ok(app):
    app.entry1.insert(ctk.END, "128")

    app.divisors_callback()
    assert "Divisors of 128" in app.label_resultat.cget("text")


def test_divisors_invalid_input(app):
    app.entry1.insert(ctk.END, "abc")

    app.divisors_callback()
    assert "Please enter a positive integer" in app.label_resultat.cget("text")


def test_divisors_invoke(app):
    app.entry1.insert(ctk.END, "10")
    app.btn_divisors.invoke()
    assert "Divisors of 10" in app.label_resultat.cget("text")
