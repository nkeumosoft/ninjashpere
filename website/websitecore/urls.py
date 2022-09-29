from django.urls import path

from websitecore.views import (
    CloudDevOpsView,
    MobileDevServiceView,
    WebDevServiceView,
    QualityAssuranceView,
    HomeView,
    TalentView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("cloud-devOps-service/", CloudDevOpsView.as_view(), name="cloud_devops"),
    path("mobile-development-service/", MobileDevServiceView.as_view(), name="mobile_dev"),
    path("web-development-service/", WebDevServiceView.as_view(), name="web_dev"),
    path("quality-assurance/", QualityAssuranceView.as_view(), name="quality_assurance"),
    path("talent/", TalentView.as_view(), name="talent"),
]
