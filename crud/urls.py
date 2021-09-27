from django.urls import path
from .views import UniversityListView , StudentListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', UniversityListView.as_view() , name="universities_list"),
    path('<slug:slug>/students', StudentListView.as_view() , name="students_list"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)