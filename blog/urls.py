from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/", views.post_detail, name="post_detail"),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/', views.PostListView.as_view(), name='post_list_by_tag'),
]
