import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)
        self.maksukortti2=Maksukortti(10)
    
    def test_oikea_maara_rahaa_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_oikea_maara_edullisia_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_oikea_maara_maukkaita_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_rahamaara_kasvaa_edullisella(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_oikea_vaihtoraha_edulliselle(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
    
    def test_myytyjen_edullisten_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_rahamaara_ei_muutu_kun_maksu_ei_riita_edulliseen(self):
        self.kassapaate.syo_edullisesti_kateisella(220)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kaikki_palautetaan_vaihtorahana_edullisesta(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
    
    def test_myytyjen_edullisten_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kortilta_veloitetaan_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
    
    def test_korttiosto_lisaa_myytyja_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortin_saldo_ei_muutu_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2)
        self.assertEqual(self.maksukortti2.saldo, 10)
    
    def test_myytyjen_maara_ei_muutu_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_palautetaan_false_kortilla_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2), False)
    
    def test_kassaraha_ei_muutu_kortilla_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_oikea_maara_maukkaita_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_rahamaara_kasvaa_maukkaalla(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_oikea_vaihtoraha_maukkaalle(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
    
    def test_myytyjen_maukkaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_rahamaara_ei_muutu_kun_maksu_ei_riita_maukkaaseen(self):
        self.kassapaate.syo_maukkaasti_kateisella(220)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kaikki_palautetaan_vaihtorahana_maukkaasta(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
    
    def test_myytyjen_maukkaiden_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kortilta_veloitetaan_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
    
    def test_korttiosto_lisaa_myytyja_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortin_saldo_ei_muutu_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2)
        self.assertEqual(self.maksukortti2.saldo, 10)
    
    def test_myytyjen_maara_ei_muutu_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_palautetaan_false_kortilla_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2), False)
    
    def test_kassaraha_ei_muutu_kortilla_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_ladattaessa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo, 1500)
    
    def test_ladattaessa_kassan_rahamaara_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
    
    def test_ei_voi_ladata_negatiivista(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
