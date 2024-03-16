from django.urls import path
from .views import ProfileList,ProfileDetail,ImageList,ImageDetails,UserLoginView,ProjectList,ProjectDetails,AdminProfileList,AdminProjectList,AdminImageList


urlpatterns = [
    path('profile/',ProfileList.as_view(),name='profile'),
    path('image/',ImageList.as_view(),name='image'),
    path('project/',ProjectList.as_view(),name='project'),

    # admin site
    path('login/',UserLoginView.as_view(),name='adminlogin'),
    path('adminprofile/',AdminProfileList.as_view(),name='adminprofile'),
    path('adminimage/',AdminImageList.as_view(),name='adminimage'),
    path('adminproject/',AdminProjectList.as_view(),name='adminproject'),
    path('adminprofile/int:<pk>/',ProfileDetail.as_view(),name='profiledetail'),
    path('adminimage/int:<pk>/',ImageDetails.as_view(),name='imagedetail'),
    path('adminproject/int:<pk>/',ProjectDetails.as_view(),name='projectdetail'),
]
