# -*- coding: utf-8 -*-

import unittest
import time
import os

from test.constants import SLEEP_BETWEEN_REQUESTS, TEST_DATA_FILE
from nmt_api import NmtAPI


class TestNmtApiHeightRequest(unittest.TestCase):
    """
    Test automatyczny do sprawdzania działania odpytywania API serwisu GUGIK
    o wysokość dla listy punktów z pliku danych testowych.
    """

    @classmethod
    def setUpClass(cls):
        """
        Przygotowanie danych testowych z pliku
        """
        data_file = os.path.join(os.path.dirname(__file__), TEST_DATA_FILE)
        cls.test_coordinates = []
        
        if not os.path.exists(data_file):
            raise FileNotFoundError(f"Plik danych testowych nie znaleziony: {data_file}")
        
        with open(data_file, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split(',')
                if len(parts) != 2:
                    continue
                x, y = float(parts[0]), float(parts[1])
                cls.test_coordinates.append((x, y))

    def testApiHeightRequestFromData(self):
        """
        Walidacja:
        - Odpowiedź nie powinna być None (brak błędu połączenia)
        - Odpowiedź nie powinna być pustym stringiem
        - Odpowiedź nie powinna być równa "0" (takie wyniki są błędne i wynikaja z tego że punkt w złym układzie współrzędnych znalazł się poza Polską)
        """
        self.assertTrue(self.test_coordinates, "Brak danych testowych do sprawdzenia")
        
        total_tests = len(self.test_coordinates)
        errors = []
        success_count = 0
        
        print(f"\n{'='*60}")
        print(f"TEST API GUGIK - Pobieranie wysokości dla {total_tests} punktów")
        print(f"Współrzędne w formacie PUWG1992 (EPSG:2180)")
        print(f"{'='*60}\n")
        
        for i, (x, y) in enumerate(self.test_coordinates, 1):
            print(f"Punkt {i}/{total_tests}: X={x:.2f}, Y={y:.2f} ... ", end='', flush=True)
            result = NmtAPI.getHbyXY(x, y)
        
            if result is None:
                error_msg = f"Punkt {i} ({x:.2f}, {y:.2f}): Błąd połączenia (wynik=None)"
                print("FAIL (Błąd połączenia)")
                errors.append(error_msg)
            elif result == "":
                error_msg = f"Punkt {i} ({x:.2f}, {y:.2f}): Pusta odpowiedź"
                print("FAIL (Pusta odpowiedź)")
                errors.append(error_msg)
            elif result == "0":
                error_msg = f"Punkt {i} ({x:.2f}, {y:.2f}): Wysokość wynosi 0 (sprawdź układ wspólrzednych)"
                print("FAIL (Wysokość=0)")
                errors.append(error_msg)
            else:
                print(f"OK (H={result}m)")
                success_count += 1
            if i < total_tests:
                time.sleep(SLEEP_BETWEEN_REQUESTS)
        
        # === PODSUMOWANIE ===
        print("\n" + "="*40)
        print("PODSUMOWANIE TESTU")
        print("="*40)
        print(f"Przetestowano: {total_tests} punktów")
        print(f"Sukcesy:       {success_count}")
        print(f"Błędy:         {len(errors)}\n")
        
        if errors:
            print("\nSzczegóły błędów:")
            for error in errors:
                print(f"  - {error}")
            print()
            self.fail(f"Test zakończony niepowodzeniem. Błędy: {len(errors)}/{total_tests}")
        else:
            print("Wszystkie punkty sprawdzone pomyślnie.\n")


if __name__ == "__main__":
    unittest.main()