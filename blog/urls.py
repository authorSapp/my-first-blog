from django.conf.urls import url
import blog.views

urlpatterns = [
    url(r'^$', 'blog.views.post_list', name='post_list'),
]
