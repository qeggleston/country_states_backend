from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from countries import views

urlpatterns = [
    path('', views.CountryList.as_view()),
    path('<str:code>/states/', include('states.urls')),
    path('<str:code>/', views.CountryDetail.as_view())
    #path('<str:code>/states')
    #path('countries/<str:code>/states', )
]