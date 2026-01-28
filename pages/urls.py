"""
Name: Evan Westcomb
Class: CIS 218
Date: 1/28/2026
"""

from django.urls import path
from .views import ContactsPageView, HomePageView, ProjectsPageView

urlpatterns = [
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('', HomePageView.as_view(), name='home'),
    path('projects/', ProjectsPageView.as_view(), name='projects'),
]