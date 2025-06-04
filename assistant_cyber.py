#!/usr/bin/env python3
"""
Assistant Cyber simple.

Ce programme propose un menu interactif avec quelques commandes utiles
pour la securite informatique.
"""

import subprocess


def show_open_ports():
    """Affiche les ports TCP/UDP ecoutes."""
    try:
        output = subprocess.check_output(["ss", "-tuln"], text=True)
        print("Listening Ports:\n")
        print(output)
    except Exception as e:
        print(f"Impossible d'afficher les ports : {e}")


def show_security_tips():
    """Affiche quelques conseils de securite."""
    tips = [
        "1. Appliquez rapidement les mises a jour de securite.",
        "2. Utilisez des mots de passe forts et uniques ou un gestionnaire de mots de passe.",
        "3. Activez l'authentification multi-facteur lorsque c'est possible.",
        "4. Sauvegardez regulierement vos donnees importantes.",
    ]
    print("\n".join(tips))


def main():
    while True:
        print(
            """\nMenu Cyber Assistant
1) Afficher les ports ouverts
2) Conseils de securite
0) Quitter
"""
        )
        choice = input("Votre choix : ").strip()
        if choice == "1":
            show_open_ports()
        elif choice == "2":
            show_security_tips()
        elif choice == "0":
            print("Au revoir.")
            break
        else:
            print("Choix invalide. Veuillez reessayer.")


if __name__ == "__main__":
    main()
