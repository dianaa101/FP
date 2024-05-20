from Service import Service
from console import Console
from entities.EvidenceSerializer import EvidenceSerializer
from repositories.FileRepository import FileRepository

evidence_serializer = EvidenceSerializer()
evidence_repo = FileRepository('evidences.txt', evidence_serializer)
evidence_service = Service(evidence_repo)
console = Console(evidence_service)
console.run()
