#!/usr/bin/env python3
"""
Assistant Cyber simple.

Ce programme propose un menu interactif avec quelques commandes utiles
pour la securite informatique.
"""

import subprocess
import shutil


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


def show_firewall_status():
    """Affiche le statut du pare-feu si disponible."""
    try:
        if shutil.which("ufw"):
            output = subprocess.check_output(["ufw", "status"], text=True)
        elif shutil.which("iptables"):
            output = subprocess.check_output(["iptables", "-L"], text=True)
        else:
            print("Aucun pare-feu detecte (ufw ou iptables).")
            return
        print("Statut du pare-feu:\n")
        print(output)
    except Exception as e:
        print(f"Impossible d'afficher le statut du pare-feu : {e}")


def show_system_updates():
    """Liste les mises a jour disponibles via APT si possible."""
    try:
        output = subprocess.check_output(
            ["apt", "list", "--upgradable"],
            text=True,
            stderr=subprocess.STDOUT,
        )
        print("Mises a jour disponibles:\n")
        print(output)
    except Exception as e:
        print(f"Impossible d'obtenir les mises a jour : {e}")


def show_last_logins():
    """Affiche les dernieres connexions."""
    try:
        output = subprocess.check_output(["last", "-n", "5"], text=True)
        print("Dernieres connexions:\n")
        print(output)
    except Exception as e:
        print(f"Impossible d'afficher les connexions : {e}")


def main():
    while True:
        print(
            """\nMenu Cyber Assistant
1) Afficher les ports ouverts
2) Conseils de securite
3) Statut du pare-feu
4) Mises a jour disponibles
5) Dernieres connexions
0) Quitter
"""
        )
        choice = input("Votre choix : ").strip()
        if choice == "1":
            show_open_ports()
        elif choice == "2":
            show_security_tips()
        elif choice == "3":
            show_firewall_status()
        elif choice == "4":
            show_system_updates()
        elif choice == "5":
            show_last_logins()
        elif choice == "0":
            print("Au revoir.")
            break
        else:
            print("Choix invalide. Veuillez reessayer.")


if __name__ == "__main__":
    main()
