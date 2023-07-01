from django.urls import path
from shop import views

urlpatterns = [
    path("", views.Shopss, name="shop"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("productview/", views.productView, name="productview"),
]
