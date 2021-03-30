import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.1")

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.lataa_rahaa(990)
        self.maksukortti.ota_rahaa(800)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")
    
    def test_nostaessa_palautuu_true(self):
        self.maksukortti.lataa_rahaa(990)
        self.assertEqual(self.maksukortti.ota_rahaa(800), True)
    
    def test_liikaa_nostaessa_palautuu_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(800), False)
    
    def test_saldo_ei_muutu_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.lataa_rahaa(190)
        self.maksukortti.ota_rahaa(800)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")