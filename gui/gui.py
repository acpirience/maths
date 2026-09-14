import customtkinter as ctk

from divisors import Divisors
from factors import Factors

# visual theme configuration
ctk.set_appearance_mode("System")  # Adapted to the system theme (Dark/Light)
ctk.set_default_color_theme("blue")


class Gui(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure the main window directly via self
        self.title("Math operations")
        self.geometry("500x400")
        self.resizable(False, False)

        # Title label
        label_titre = ctk.CTkLabel(
            self,
            text="Math operations",
            font=ctk.CTkFont(size=18, weight="bold"),
        )
        label_titre.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        # Field 1
        self.entry1 = ctk.CTkEntry(self, placeholder_text="first number", width=250)
        self.entry1.grid(row=1, column=0, columnspan=3, padx=20, pady=8)

        # Field 2: used only for PGCD and PPCM, for future uses
        self.entry2 = ctk.CTkEntry(self, placeholder_text="second number", width=250)
        self.entry2.grid(row=2, column=0, columnspan=3, padx=20, pady=8)

        # buttons
        self.btn_divisors = ctk.CTkButton(
            self, text="Divisors", command=self.divisors_callback, width=100
        )
        self.btn_divisors.grid(row=4, column=1, padx=20, pady=20)

        self.btn_factors = ctk.CTkButton(
            self, text="Factors", command=self.factors_callback, width=100
        )
        self.btn_factors.grid(row=4, column=2, padx=20, pady=20)

        # label for result or error messages
        self.label_resultat = ctk.CTkLabel(
            self, text="", font=ctk.CTkFont(size=14, weight="bold")
        )
        self.label_resultat.grid(row=5, column=0, columnspan=3, padx=20, pady=20)

    def divisors_callback(self):
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

            divisors = Divisors(n1)
            _ = divisors.get_divisors()
            self.label_resultat.configure(
                text=f"Divisors of {n1} : {divisors.pretty_print_factors()}",
                text_color=("green", "#2ecc71"),
                wraplength=380,
            )
        except ValueError as error:
            self.label_resultat.configure(
                text=error,
                text_color=("red", "#e74c3c"),
            )

    def factors_callback(self):
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

            factors = Factors(n1)
            _ = factors.factorise()
            self.label_resultat.configure(
                text=f"Factors of {n1} : {factors.pretty_print_factors()}",
                text_color=("green", "#2ecc71"),
                wraplength=380,
            )
        except ValueError as error:
            self.label_resultat.configure(
                text=error,
                text_color=("red", "#e74c3c"),
            )
