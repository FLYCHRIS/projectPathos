from django.urls import path
from . import views

app_name = "equipmentFinder"
urlpatterns = [
    path("equip-search/", views.searchPage, name='equipSearchPage'),
    path("add-equip/", views.addEquipmentPage, name='addEquipmentPage'),
    path("search-results/", views.searchResultsPage, name='searchResultsPage')
]