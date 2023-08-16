from rest_framework.response import Response
from rest_framework.views import APIView

from apps.jobhunt.models import Vacancy, Company, Resume


class StatisticsAPIView(APIView):
    def get(self, request):
        vacancy = Vacancy.objects.all().count()
        company = Company.objects.all().count()
        resume = Resume.objects.all().count()

        data = {
            'Count of Vacancies ': vacancy,
            'Count of Companies ': company,
            'Count of Resumes ': resume
        }
        return Response(data)
