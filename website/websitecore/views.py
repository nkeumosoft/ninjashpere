from django.shortcuts import render

from django.views import View
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "websitecore/index.html"

    def get(self, request, *args, **kwargs):
        # context = {"navbar": "home"}
        return render(request, self.template_name, {})


class TalentView(TemplateView):
    template_name = "websitecore/talent.html"

    def get(self, request, *args, **kwargs):
        # context = {"navbar": "talent"}
        return render(request, self.template_name, {})


class CloudDevOpsView(View):
    template_name = "websitecore/cloud&devOps-service.html"

    def get(self, request, *args, **kwargs):
        # context = {"navbar": "cloud_devops"}
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        ...


class MobileDevServiceView(View):
    template_name = "websitecore/mobile-development-service.html"

    def get(self, request, *args, **kwargs):
        # context = {"navbar": "mobile_dev"}
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        ...


class WebDevServiceView(View):
    template_name = "websitecore/web-development-service.html"

    def get(self, request, *args, **kwargs):
        # context = {"navbar": "web_dev"}
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        ...


class QualityAssuranceView(View):
    template_name = "websitecore/quality-assurance.html"

    def get(self, request, *args, **kwargs):
        # context = {"navbar": "quality_assurance"}
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        ...


class KnowledgeView(TemplateView):
    template_name = "websitecore/knowledge.html"

    def get(self, request, *args, **kwargs):
        # context = {"navbar": "knowledge"}
        return render(request, self.template_name, {})


class CaseStudyView(View):
    template_name = "websitecore/case-study.html"

    def get(self, request, *args, **kwargs):
        # context = {"navbar": "knowledge"}
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        ...
