from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('studentdetails',views.StudentViewSet)
router.register('studentMarkdetails',views.MarkViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
