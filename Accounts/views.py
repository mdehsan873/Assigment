from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Company, Team
from .serializer import RegistrationSerializer, CompanySerializer, TeamSerializer


# Create your views here.
class SuperAdminRegistration(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        print(request.data)
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CompanySerializer

    def post(self, request):
        company = request.data.get('company', {})
        serializer = self.serializer_class(data=company)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamAPIView(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = TeamSerializer

    def get(self, request):
        companies = Company.objects.all()
        data = []
        for company in companies:
            team = Team.objects.filter(companyID=company)
            serializer = self.serializer_class(team, many=True)
            data.extend(serializer.data)
        return Response({'data': data}, status=status.HTTP_200_OK)

    def post(self, request, companyID):
        team = request.data.get('team', {})
        if not Company.objects.filter(uuid=companyID).exists():
            return Response({"error": "Please provide valid company uuid"})
        company = Company.objects.get(uuid=companyID)
        print(company.name)
        team.__setitem__('companyID', company.uuid)
        serializer = self.serializer_class(data=team)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanySearchAPIView(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = CompanySerializer

    def get(self, request):
        id = request.GET.get('id', None)
        name = request.GET.get('name', None)
        if not id and not name:
            return Response({"error": "Please provide search query"}, status=status.HTTP_400_BAD_REQUEST)
        if id:
            company = Company.objects.filter(uuid=id)
        if name:
            company = Company.objects.filter(name=name)

        serializer = self.serializer_class(company, many=True)
        if len(serializer.data) == 0:
            return Response({"msg": "No company found"}, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)
