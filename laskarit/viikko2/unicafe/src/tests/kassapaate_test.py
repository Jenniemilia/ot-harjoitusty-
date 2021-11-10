import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassassa_on_alussa_oikea_maara_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisten_saldo_on_alussa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukkaiden_saldo_on_alussa_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisnosto_toimii_maukkaalla(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisnosto_toimii_edullisella(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(vaihtoraha, 260)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisnosto_toimii_jos_maksu_ei_ole_riittävä_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisnosto_toimii_jos_maksu_ei_ole_riittävä_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maksukortti_toimii_maukkaalla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0", "True")
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_maksukortti_toimii_edullisella(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 7.6", "True")
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maksukortti_toimii_jos_ei_saldoa_maukkaalla(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti), "saldo: 2.0", "False")
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_maksukortti_toimii_jos_ei_saldoa_edullisella(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti), "saldo: 2.0", "False")
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)   

    def test_kortille_ladatessa_saldo_muuttuu_kortti(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")

    def test_kortille_ladatessa_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_kortille_ei_voi_ladata_negatiivista_lukua_kassa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_kortille_ei_voi_ladata_negatiivista_lukua_kortti(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)