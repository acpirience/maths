import customtkinter as ctk

from divisors import Divisors
from factors import Factors
from prime import is_prime

# visual theme configuration
ctk.set_appearance_mode("System")  # Adapted to the system theme (Dark/Light)
ctk.set_default_color_theme("blue")

WIDTH = 500
HEIGHT = 400
NB_BUTTONS = 3
PADX = 20
PADY = 20
WIDTH_BUTTONS: int = (WIDTH - PADX * 2) // (NB_BUTTONS + 1)


class Gui(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure the main window directly via self
        self.title("Math operations")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.resizable(False, False)

        # Title label
        label_titre = ctk.CTkLabel(
            self,
            text="Math operations",
            font=ctk.CTkFont(size=18, weight="bold"),
        )
        label_titre.grid(row=0, column=1, columnspan=NB_BUTTONS, padx=PADX, pady=PADY)

        # Field 1
        self.entry1 = ctk.CTkEntry(
            self, placeholder_text="first number", width=WIDTH // 2
        )
        self.entry1.grid(row=1, column=0, columnspan=NB_BUTTONS, padx=PADX, pady=8)

        # Field 2: used only for PGCD and PPCM, for future uses
        self.entry2 = ctk.CTkEntry(
            self, placeholder_text="second number", width=WIDTH // 2
        )

        self.entry2.grid(row=2, column=0, columnspan=NB_BUTTONS, padx=PADX, pady=8)

        # buttons
        self.btn_divisors = ctk.CTkButton(
            self, text="Divisors", command=self.divisors_callback, width=WIDTH_BUTTONS
        )
        self.btn_divisors.grid(row=4, column=1, padx=PADX, pady=PADY)

        self.btn_factors = ctk.CTkButton(
            self, text="Factors", command=self.factors_callback, width=WIDTH_BUTTONS
        )
        self.btn_factors.grid(row=4, column=2, padx=PADX, pady=PADY)

        self.btn_prime = ctk.CTkButton(
            self, text="Prime ?", command=self.prime_callback, width=WIDTH_BUTTONS
        )
        self.btn_prime.grid(row=4, column=3, padx=PADX, pady=PADY)

        # label for result or error messages
        self.label_resultat = ctk.CTkLabel(
            self, text="", font=ctk.CTkFont(size=14, weight="bold")
        )
        self.label_resultat.grid(
            row=5, column=1, columnspan=NB_BUTTONS, padx=PADX, pady=PADY
        )

    def divisors_callback(self, event=None):
        try:
            val1 = self.entry1.get().strip()
            n1 = int(val1)  # Raises ValueError if string is not an integer

            divisors = Divisors(n1)  # May raise ValueError (e.g., if negative or zero)
            _ = divisors.get_divisors()

            self.label_resultat.configure(
                text=f"Divisors of {n1} : {divisors.pretty_print_factors()}",
                text_color=("green", "#2ecc71"),
                wraplength=380,
            )

        except ValueError:
            self.label_resultat.configure(
                text=f"Please enter a positive integer: {val1}",
                text_color=("red", "#e74c3c"),
                wraplength=380,
            )

    def factors_callback(self):
        try:
            val1 = self.entry1.get().strip()
            n1 = int(val1)

            factors = Factors(n1)
            _ = factors.get_factors()
            self.label_resultat.configure(
                text=f"Factors of {n1} : {factors.pretty_print_factors()}",
                text_color=("green", "#2ecc71"),
                wraplength=380,
            )
        except ValueError:
            self.label_resultat.configure(
                text=f"Please enter a positive integer: {val1}",
                text_color=("red", "#e74c3c"),
                wraplength=380,
            )

    def prime_callback(self):
        try:
            val1 = self.entry1.get().strip()
        except ValueError as e:
            self.label_resultat.configure(
                text=f"Please enter a positive integer: {e}",
                text_color=("red", "#e74c3c"),
            )
            return

        try:
            n1 = int(val1)

            if is_prime(n1):
                self.label_resultat.configure(
                    text=f"{n1} is prime.",
                    text_color=("green", "#2ecc71"),
                )
            else:
                self.label_resultat.configure(
                    text=f"{n1} is not prime.",
                    text_color=("red", "#e7cb3c"),
                )
        except ValueError as error:
            self.label_resultat.configure(
                text=error,
                text_color=("red", "#e74c3c"),
            )
