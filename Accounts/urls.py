from django.urls import path
from .views import CompanyAPIView, TeamAPIView, CompanySearchAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('get/superuser/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("company/create/", CompanyAPIView.as_view(), name="companyView"),
    path("team/create/<companyID>/", TeamAPIView.as_view(), name="teamView"),
    path("get/all/team/", TeamAPIView.as_view(), name="allTeam"),
    path("company/search/", CompanySearchAPIView.as_view(), name="searchCompany")
]
