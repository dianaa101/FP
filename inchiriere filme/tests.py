from entities.Customer import Customer
from entities.Entity import Entity
from entities.Movie import Movie
from repo.Repository import Repository
from service.CustomerService import CustomerService
from service.MovieService import MovieService
from service.RentMovieService import RentMovieService
from validator.CustomerValidator import CustomerValidator
from validator.MovieValidator import MovieValidator


def test_entity():
    e = Entity(0)
    assert e.get_id() == 0
    e.set_id(100)
    assert e.get_id() == 100
    e.set_multiple(id_=9)
    assert e.get_id() == 9


def test_movie():
    e = Movie(1, 'Mota', 'Mehhhhhhhh', 'Horror')
    assert e.get_title() == 'Meh'
    e.set_title('Whatever')
    assert e.get_title() == 'Whatever'

    assert e.get_description() == 'Mehhhhhhhh'
    e.set_description('SKSKSKSK')
    assert e.get_description() == 'SKSKSKSK'

    assert e.get_genre() == 'Horror'
    e.set_genre('Nimica')
    assert e.get_genre() == 'Nimica'


def test_repo():
    repo = Repository()
    e = Entity(0)
    repo.add(e)
    es = repo.get_all()
    assert len(es) == 1
    assert es[0] == e

    ef = repo.find_by_id(0)
    assert ef == e

    repo.update(0, id_=1)
    assert e.get_id() == 1

    er = repo.remove_by_id(1)
    assert er == e


def test_customer():
    e = Customer(0, 'Mota', '1234567891111', 0)
    assert e.get_name() == 'Mota'
    e.set_name('Cosmin')
    assert e.get_name() == 'Cosmin'

    assert e.get_cnp() == '1234567891111'
    e.set_cnp('98765432198765')
    assert e.get_cnp() == '98765432198765'

    assert e.get_number_of_rents() == 0
    e.set_number_of_rents(10)
    assert e.get_number_of_rents() == 10


def test_customer_service():
    repo = Repository()
    validator = CustomerValidator()
    service = CustomerService(validator, repo)
    s = service.create('Mota', '1234567891011')
    assert s.get_name() == 'Mota'
    assert s.get_cnp() == '1234567891011'
    ss = service.get_all()
    assert len(ss) == 1
    assert ss[0] == s
    s = service.update(s.get_id(), 'Mom', '1234567891011')
    assert s.get_name == 'Mom'
    assert s.get_cnp == '1234567891011'
    service.remove(s.get_id())
    ss = service.get_all()
    assert len(ss) == 0


def test_movie_service():
    repo = Repository()
    validator = MovieValidator()
    service = MovieService(validator, repo)
    s = service.create('LMAO', 'Funny movie here', 'Comedy')
    assert s.get_title() == 'LMAO'
    assert s.get_description() == 'Funny movie here'
    assert s.get_genre() == 'Comedy'
    ss = service.get_all()
    assert len(ss) == 1
    assert ss[0] == s
    s = service.update(s.get_id(), 'LMAO', 'Not funny actually', 'Comedy')
    assert s.get_title() == 'LMAO'
    assert s.get_description() == 'Not funny actually'
    assert s.get_genre() == 'Comedy'
    service.remove(s.get_id)
    ss = service.get_all()
    assert len(ss) == 0


def test_validator():
    validator = MovieValidator()
    movie = Movie(0, 'Lmao', 'Blah', 'Horror', None, 0)
    validator.validate_movie(movie)

    movie = Movie(0, '', 'Blah', 'Horror', None, 0)
    try:
        validator.validate_movie(movie)
        assert False
    except ValueError:
        pass


def test_get_customers_with_rented_movies():
    customer_validator = CustomerValidator()
    customer_repo = Repository()
    customer_service = CustomerService(customer_validator, customer_repo)
    movie_validator = MovieValidator()
    movie_repo = Repository()
    movie_service = MovieService(movie_validator, movie_repo)
    rent_movie_service = RentMovieService(movie_repo, customer_repo)
    a = customer_service.create('Mota', '1234567891011')
    b = customer_service.create('Cosmin', '98727378282')
    c = customer_service.create('Screech', '123493983984')

    movie_1 = movie_service.create('LMAO', 'Blaaaaa', 'Mota')
    movie_2 = movie_service.create('Screech', 'Cat is gay', 'Lesbian')

    rent_movie_service.rent_movie(a.get_id(), movie_1.get_id())
   # rent_movie_service.return_movie(a.get_id(), movie_1.get_id())

    rent_movie_service.rent_movie(b.get_id(), movie_2.get_id())
   # rent_movie_service.return_movie(b.get_id(), movie_2.get_id())

    customers = customer_service.get_customers_with_rented_movies()
    assert len(customers) == 2
    assert customers[0].get_id() == a.get_id()
    assert customers[1].get_id() == b.get_id()


def test_get_top_30p_customers_with_rented_movies():
    customer_validator = CustomerValidator()
    customer_repo = Repository()
    customer_service = CustomerService(customer_validator, customer_repo)
    movie_validator = MovieValidator()
    movie_repo = Repository()
    movie_service = MovieService(movie_validator, movie_repo)
    rent_movie_service = RentMovieService(movie_repo, customer_repo)
    a = customer_service.create('Mota', '1234567891011')
    b = customer_service.create('Cosmin', '98727378282')

    movie_1 = movie_service.create('LMAO', 'Blaaaaa', 'Mota')
    movie_2 = movie_service.create('Screech', 'Cat is gay', 'Lesbian')
    movie_3 = movie_service.create('Cake', 'Clingy Cat', 'LovesMen')

    rent_movie_service.rent_movie(a.get_id(), movie_1.get_id())
    rent_movie_service.rent_movie(b.get_id(), movie_2.get_id())
    rent_movie_service.rent_movie(a.get_id(), movie_3.get_id())

    customers = customer_service.get_top_30p_customers_with_rented_movies()
    assert len(customers) == 1
    assert customers[0].get_id() == a.get_id()


def run_tests():
    test_entity()
    test_movie()
    test_repo()
    test_customer()
    test_customer_service()
    test_movie_service()
    test_validator()
    test_get_customers_with_rented_movies()
    test_get_top_30p_customers_with_rented_movies()
