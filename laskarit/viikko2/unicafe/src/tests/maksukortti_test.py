import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_on_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")

    def test_saldo_vahenee_oikein_jos_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")

    def test_saldo_ei_muutu_jos_ei_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(30)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_metodi_palauttaa_false_jos_saldo_menee_yli(self):
        self.maksukortti.ota_rahaa(50)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1", "False")

    def test_metodi_palauttaa_true_jos_saldo_riittaa(self):
        self.maksukortti.ota_rahaa(4)
        self.assertEqual(str(self.maksukortti), "saldo: 0.06", "True")