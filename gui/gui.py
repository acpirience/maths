import customtkinter as ctk

# visual theme configuration
ctk.set_appearance_mode("System")  # Adapted to the system theme (Dark/Light)
ctk.set_default_color_theme("blue")


class Gui(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Création de la fenêtre principale
        app = ctk.CTk()
        app.title("Multiplicateur d'entiers")
        app.geometry("400x320")
        app.resizable(False, False)

        # Titre principal
        label_titre = ctk.CTkLabel(
            app,
            text="Calculateur de Multiplication",
            font=ctk.CTkFont(size=18, weight="bold"),
        )
        label_titre.pack(pady=(20, 15))

        # Champ 1
        self.entry1 = ctk.CTkEntry(
            app, placeholder_text="Premier nombre entier", width=250
        )
        self.entry1.pack(pady=8)

        # Champ 2
        self.entry2 = ctk.CTkEntry(
            app, placeholder_text="Second nombre entier", width=250
        )
        self.entry2.pack(pady=8)

        # Bouton de calcul
        self.btn_calculer = ctk.CTkButton(
            app, text="Multiplier", command=self.effectuer_multiplication, width=250
        )
        self.btn_calculer.pack(pady=15)

        # Label d'affichage du résultat ou de l'erreur
        self.label_resultat = ctk.CTkLabel(
            app, text="", font=ctk.CTkFont(size=14, weight="bold")
        )
        self.label_resultat.pack(pady=10)

    def effectuer_multiplication(self):
        # Récupération de la saisie utilisateur
        val1 = self.entry1.get().strip()
        val2 = self.entry2.get().strip()

        # Validation : vérification des entiers (gère aussi les nombres négatifs)
        try:
            n1 = int(val1)
            n2 = int(val2)

            # Calcul et affichage du résultat
            resultat = n1 * n2
            self.label_resultat.configure(
                text=f"Résultat : {n1} × {n2} = {resultat}",
                text_color=("green", "#2ecc71"),
            )
        except ValueError:
            # Affichage d'un message d'erreur si la saisie n'est pas un entier valide
            self.label_resultat.configure(
                text="Erreur : veuillez saisir deux nombres entiers valides !",
                text_color=("red", "#e74c3c"),
            )
