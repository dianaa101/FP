from Console import Console
from Service import Service
from entities.ActivitySerializer import ActivitySerializer
from repositories.FileRepository import FileRepository

activity_serializer = ActivitySerializer()
activity_repo = FileRepository('activities.txt', activity_serializer)
activity_service = Service(activity_repo)
console = Console(activity_service)
console.run()
