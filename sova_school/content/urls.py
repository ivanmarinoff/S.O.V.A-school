from django.urls import path
from sova_school.content.views import ReadContentView, CreateContentView, EditContentView, DeleteContentView, \
    DetailContentView, ContentListView
from django.urls import path


urlpatterns = (
    path('read_content/<slug:slug>/', ReadContentView.as_view(), name='read-content'),
    path('detail_content/<slug:slug>/', DetailContentView.as_view(), name='detail-content'),
    path('create_content/<int:pk>/', CreateContentView.as_view(), name='create-content'),
    path('edit_content/<slug:slug>/', EditContentView.as_view(), name='edit-content'),
    path('delete_content/<slug:slug>/', DeleteContentView.as_view(), name='delete-content'),
    path('content/', ContentListView.as_view(), name='content-list'),
)


