from django.urls import path,include
from Practice.views import StudentView,NOTPKStudentView,PKStudentView,StudentViewSet,StudentRetrieveUpdateDestroy,StudentModelview
from rest_framework import routers
router=routers.DefaultRouter()
router.register('test',StudentViewSet,basename='test')
router.register('practice',StudentModelview,basename='practice')
urlpatterns=[
    # path('',StudentView.as_view()),
    # path('<int:pk>',StudentView.as_view())
    # path('',NOTPKStudentView.as_view()),
    # path('<int:pk>/',PKStudentView.as_view())
    path('sachin/',include(router.urls)),
    path('anant/<int:pk>',StudentRetrieveUpdateDestroy.as_view())

]