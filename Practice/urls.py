from django.urls import path,include
from Practice.views import StudentView,NOTPKStudentView,PKStudentView
urlpatterns=[
    # path('',StudentView.as_view()),
    # path('<int:pk>',StudentView.as_view())
    path('',NOTPKStudentView.as_view()),
    path('<int:pk>/',PKStudentView.as_view())
]