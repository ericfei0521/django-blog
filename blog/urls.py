from django.urls import re_path
from blog import views

urlpatterns = [
    re_path(r"^$", views.PostsListViews.as_view(), name="posts_list"),
    re_path(r"^about/$", view=views.AboutView.as_view(), name="about"),
    re_path(r"^post/(?P<pk>\d+)$", views.DetailView.as_view(), name="post_detail"),
    re_path(r"^post/new/$", views.CreatePostView.as_view(), name="post_new"),
    re_path(
        r"^post/(?P<pk>\d+)/edit/$", views.UpdatePostView.as_view(), name="post_edit"
    ),
    re_path(
        r"^post/(?P<pk>\d+)/delete/$",
        views.DeletePostView.as_view(),
        name="post_delete",
    ),
    re_path(
        r"^drafts/$",
        views.DraftPostsView.as_view(),
        name="post_drafts_list",
    ),
    re_path(
        r"^post/(?P<pk>\d+)/comment/$",
        views.add_comment_to_post,
        name="add_comment_to_post",
    ),
    re_path(
        r"^comment/(?P<pk>\d+)/approve/$",
        views.comment_approve,
        name="comment_approve",
    ),
    re_path(
        r"^comment/(?P<pk>\d+)/remove/$",
        views.comment_remove,
        name="comment_remove",
    ),
    re_path(
        r"^post/(?P<pk>\d+)/publish/$",
        views.post_publish,
        name="post_publish",
    ),
]
