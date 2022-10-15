from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name='home'),
    path('events', views.all_events, name='event-list'),
    path('add-venue', views.add_venue, name='add_venue'),
    path('list-venue', views.list_venue, name='list_venue'),
    path('detail-view/<str:pk>/', views.venue_detail, name='venue_detail'),
    path('search_venue/', views.search_venue, name='search_venue'),
    path('update_venue/<str:pk>/', views.update_venue, name='update_venue'),
    path('add-event', views.add_event, name='add_event'),
    path('update_event/<str:pk>/', views.update_event, name='update_event'),
    path('delete_event/<str:pk>/', views.delete_event, name='delete_event'),
    path('delete_venue/<str:pk>/', views.delete_venue, name='delete_venue'),
    path('venue_text', views.venue_text, name='venue_text'),
    path('venue_csv', views.venue_csv, name='venue_csv'),
    path('venue_pdf', views.venue_pdf, name='venue_pdf'),
]

