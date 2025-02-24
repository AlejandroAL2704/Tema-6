import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen

class TestApp(unittest.TestCase):
    def test_hola_mundo(self):
        # Inicia el servidor en un hilo aparte para las pruebas
        # Simula una petición GET
        response = urlopen('http://localhost:8000').read()
        self.assertEqual(response, b"Hola Mundo!")

if __name__ == "__main__":
    unittest.main()
