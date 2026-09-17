import customtkinter as ctk
import pytest

from gui import Gui


@pytest.fixture
def app():
    app = Gui()
    yield app


#   app.destroy()


# Divisors tests
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


# Factors tests
def test_factors_ok(app):
    app.entry1.insert(ctk.END, "60")

    app.factors_callback()
    assert "Factors of 60" in app.label_resultat.cget("text")


def test_factors_invalid_input(app):
    app.entry1.insert(ctk.END, "abc")

    app.factors_callback()
    assert "Please enter a positive integer" in app.label_resultat.cget("text")


def test_factors_invoke(app):
    app.entry1.insert(ctk.END, "60")
    app.btn_factors.invoke()
    assert "Factors of 60" in app.label_resultat.cget("text")


# Prime tests
def test_prime_ok(app):
    app.entry1.insert(ctk.END, "7")

    app.prime_callback()
    assert "7 is prime." in app.label_resultat.cget("text")


def test_prime_ko(app):
    app.entry1.insert(ctk.END, "8   ")

    app.prime_callback()
    assert "8 is not prime." in app.label_resultat.cget("text")


def test_prime_invalid_input(app):
    app.entry1.insert(ctk.END, "abc")

    app.prime_callback()
    assert "Please enter a positive integer" in app.label_resultat.cget("text")


def test_prime_invoke(app):
    app.entry1.insert(ctk.END, "7")
    app.btn_prime.invoke()
    assert "7 is prime." in app.label_resultat.cget("text")
