from django.urls import path
from kibi.views import PostListView, PostDetailView


urlpatterns = [
    path('', PostListView.as_view(), name='kibi-list-post'),
    path('<str:slug>/', PostDetailView.as_view(), name='kibi-details-post'),
]