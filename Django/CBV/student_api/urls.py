from django.urls import path, include
from rest_framework import routers
from .views import (
    home,
    # ! fuction views
    # students_list,
    # student_create,
    # student_detail,
    # student_update,
    # student_delete,
    # student_api,
    # student_api_get_update_delete
    # ! class views
    # StudentListCreate,
    # StudentDetail,
    # StudentGAV,
    # StudentDetailGAV,
    # StudentCV,
    # StudentDetailCV
    StudentMVS,
)
router = routers.DefaultRouter()
router.register("student", StudentMVS)

urlpatterns = [
    path("", home),
    # ! fuction views

    # path("student-list/", students_list, name='list'),
    # path("student-create/", student_create, name='create'),
    # path("student-detail/<int:pk>/", student_detail, name='detail'),
    # path("student-update/<int:pk>/", student_update, name='update'),
    # path("student-delete/<int:pk>/", student_delete, name='delete'),
    # path('student/', student_api),
    # path('student/<int:pk>', student_api_get_update_delete)
    # ! class views
    # path("student/", StudentListCreate.as_view()),
    # path("student/<int:pk>", StudentDetail.as_view())
    #! mixins
    # path("student/", StudentGAV.as_view()),
    # path("student/<int:pk>", StudentDetailGAV.as_view()),

    #! concrete
    # path("student/", StudentCV.as_view()),
    # path("student/<int:pk>", StudentDetailCV.as_view()),
    #! viewset
    path("", include(router.urls))

]
