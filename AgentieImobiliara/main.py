from Service import Service
from console import Console
from entities.ResidenceSerializer import ResidenceSerializer
from repositories.FileRepository import FileRepository

residence_serializer = ResidenceSerializer()
residence_repo = FileRepository('residences.txt', residence_serializer)
residence_service = Service(residence_repo)
console = Console(residence_service)
console.run()
