from django.urls import path

from catalog.views import CatalogView,CreateimageView

urlpatterns = [
    path("",CatalogView.as_view(),name='catalog'),
    path("create_image/",CreateimageView.as_view(),name='createimage')

]
