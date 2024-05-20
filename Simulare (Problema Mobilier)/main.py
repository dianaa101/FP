from entities.FurnitureSerializer import FurnitureSerializer
from entities.Mobilier import Mobilier
from repo.FileRepository import FileRepository
from repo.Repository import Repository
from service.MobilierService import MobilierService
from validator.EntityValidator import EntityValidator
from validator.MobilierValidator import MobilierValidator
from ui.Console import Console
from tests import run_tests

furniture_serializer = FurnitureSerializer()
repo_furniture = FileRepository('furniture.txt', furniture_serializer)
validator_furniture = MobilierValidator()
service_furniture = MobilierService(validator_furniture, repo_furniture)
console = Console(service_furniture)

console.run()
run_tests()



