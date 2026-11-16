"""Test de non-régression pour SQLi.sqli_low (injection SQL corrigée).

Lancement depuis TIWAP/ : python3 -m unittest discover -s tests -v
"""
import os
import shutil
import sqlite3
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# DBManager ouvre 'TIWAP.db' en chemin relatif à l'import : on travaille sur une copie
_tmp = tempfile.mkdtemp()
shutil.copy(os.path.join(ROOT, "TIWAP.db"), _tmp)
os.chdir(_tmp)
sys.path.insert(0, ROOT)

from vulnerabilities import SQLi  # noqa: E402


class SqliLowTest(unittest.TestCase):
    def test_payload_classique_ne_renvoie_aucun_utilisateur(self):
        result = SQLi.sqli_low("x' OR '1'='1' --", "peu importe")
        self.assertEqual(result, [])

    def test_quote_dans_le_mot_de_passe_ne_casse_pas_la_requete(self):
        result = SQLi.sqli_low("inconnu", "l'apostrophe")
        self.assertNotIsInstance(result, sqlite3.Error)
        self.assertEqual(result, [])

    def test_utilisateur_inconnu(self):
        self.assertEqual(SQLi.sqli_low("inconnu", "mdp"), [])

    def test_utilisateur_existant_inchange(self):
        self.assertEqual(SQLi.sqli_low("admin", "mdp"), "User Exists")


if __name__ == "__main__":
    unittest.main()
