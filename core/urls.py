from django.contrib import admin
from django.urls import path
from .import views
from .views import PostListView,about,PostDetailView,PostCreate,Update
urlpatterns = [
   # path('', admin.site.urls),
   path('about/',views.about,name="blog-about"),

   path('',PostListView.as_view(),name="blog-home"),
   path('create/',PostCreate.as_view(),name="blog-create"),
   path('post/<int:pk>/update/',Update.as_view(),name="blog-update"),


   path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),

]
