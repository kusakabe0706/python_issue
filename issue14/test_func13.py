# テスト対象の関数を読み込む
from func13 import add

def test_add_normal():
    # 3 + 5 + 7 = 15 になるかテスト
    assert add(3, 5, 7) == 15

def test_add_negative():
    # マイナスの値を入れても正しく計算されるかテスト
    assert add(-1, -2, -3) == -6

def test_add_zero():
    # 0 を入れても正しく計算されるかテスト
    assert add(0, 0, 0) == 0