from entities.Mobilier import Mobilier

def test_mobilier():
    m = Mobilier(0, 'corp iluminat', 'lampa Venetia', 12, 500)
    assert m.get_id() == 0
    m.set_id(1)
    assert m.get_id() == 1

    assert m.get_type() == 'corp iluminat'

    assert m.get_name() == 'lampa Venetia'
    m.set_name('lampa de birou')
    assert m.get_name() == 'lampa de birou'

    assert m.get_price() == 12

    assert m.get_available_stock() == 500

def run_tests():
    test_mobilier()