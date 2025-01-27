import unittest
from src.puyo import Puyo
from src.puyopair import PuyoPair
from src.nextpuyo import NextPuyo
from src.field import Field
from src.game import Game

class TestPuyo(unittest.TestCase):
    def test_puyo_initialization(self):
        p = Puyo('RED')
        self.assertEqual(p.color, 'RED')

    def test_draw_method(self):
        import pygame
        pygame.init()
        display = pygame.display.set_mode((800, 600))
        
        p = Puyo('RED')
        p.draw(1, 1)
        
        # 描画されたぷよの色が赤であることを確認
        pixel_color = display.get_at((1 * 20 + 10, 1 * 20 + 10))  # CELL_WIDTH=20と仮定
        self.assertEqual(pixel_color.r, 255)  # 赤のR成分は255

class TestPuyoPair(unittest.TestCase):
    def test_initialization(self):
        pair = PuyoPair(None, None)
        self.assertIsNotNone(pair.puyo_main)
        self.assertIsNotNone(pair.puyo_sub)

    def test_rotate_method(self):
        pair = PuyoPair()
        initial_state = pair.rotation_state
        
        pair.rotate('CLOCKWISE')
        new_state = pair.rotation_state
        
        self.assertNotEqual(initial_state, new_state)

class TestNextPuyo(unittest.TestCase):
    def test_initialization_with_none(self):
        next_p = NextPuyo()
        self.assertIsNone(next_p.puyo_main)
        self.assertIsNone(next_p.puyo_sub)

    def test_set_next_puyopair(self):
        next_p = NextPuyo()
        puyo_pair = PuyoPair()
        
        next_p.set_next_puyopair(puyo_pair)
        
        self.assertEqual(next_p.puyo_main.color, puyo_pair.puyo_main.color)
        self.assertEqual(next_p.puyo_sub.color, puyo_pair.puyo_sub.color)

class TestField(unittest.TestCase):
    def setUp(self):
        self.field = Field()

    def test_set_and_get_puyo(self):
        p = Puyo('RED')
        self.field.set_puyo(0, 0, p)
        
        retrieved_puyo = self.field.get_puyo(0, 0)
        self.assertEqual(retrieved_puyo.color, p.color)
        
        # 不正な位置への設定を確認
        with self.assertRaises(IndexError):
            self.field.set_puyo(-1, -1, Puyo('BLUE'))


if __name__ == '__main__':
    unittest.main()
