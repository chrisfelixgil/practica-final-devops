import unittest
from bs4 import BeautifulSoup
import os

class TestIndexHTML(unittest.TestCase):

    def setUp(self):
        script_dir = os.path.dirname(__file__) 
        rel_path = "../index.html"
        abs_file_path = os.path.join(script_dir, rel_path)
        try:
            with open(abs_file_path, 'r', encoding='utf-8') as f:
                self.html_content = f.read()
            self.soup = BeautifulSoup(self.html_content, 'html.parser')
        except FileNotFoundError:
            self.fail(f"index.html no encontrado en la ruta esperada: {abs_file_path}")
        except Exception as e:
            self.fail(f"Error al leer  index.html: {e}")

    def test_title_exists(self):
        """Prueba si el documento HTML tiene una etiqueta <title>."""
        title_tag = self.soup.find('title')
        self.assertIsNotNone(title_tag, "La etiqueta <title> no se encontró en index.html")
        self.assertNotEqual(title_tag.string.strip(), "", "La etiqueta <title> no debe estar vacía")

    def test_h1_exists(self):
        """Prueba si el documento HTML tiene exactamente una etiqueta <h1>."""
        h1_tags = self.soup.find_all('h1')
        self.assertEqual(len(h1_tags), 1, "Debe haber exactamente una etiqueta <h1> en index.html")
        if h1_tags:
             self.assertNotEqual(h1_tags[0].string.strip(), "", "La etiqueta <h1> no debe estar vacía")

if __name__ == '__main__':
    unittest.main() 