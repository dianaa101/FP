from entities.Entity import Entity
from entities.Book import Book
from entities.Customer import Customer


def test_entity():
    e = Entity(0)
    assert e.get_id() == 0
    e.set_id(1)
    assert e.get_id() == 1
    e.set_multiple(id_=2)
    assert e.get_id() == 2


def test_book():
    e = Book(0, 'Haunting Adeline', 'Screech', 'Bla bla bla')
    assert e.get_title() == 'Haunting Adeline'
    e.set_title('I love fur')
    assert e.get_title() == 'I love fur'
    e.set_multiple(title='I love leggy')
    assert e.get_title() == 'I love leggy'

# TODO: mota tests :(


def run_tests():
    test_entity()
    test_book()