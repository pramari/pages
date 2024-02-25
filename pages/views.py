from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class TagView(View):
    def get(self, request):
        from pages.models import MethodPage
        pages = MethodPage.objects.filter(tags__in=['method'])
        return HttpResponse(pages)
