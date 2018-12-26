from core.models import Answer

__all__ = [
    'AnswerService'
]


class AnswerService:
    def get_queryset(self):
        return Answer.objects.get_queryset()

    def create(self, name: str, email: str, university: str) -> Answer:
        answer = Answer()
        answer.name = name
        answer.email = email
        answer.university = university
        answer.save()
        return answer
    