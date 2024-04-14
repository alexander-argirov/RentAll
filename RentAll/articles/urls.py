from django.urls import path

from RentAll.articles.views import CommonArticlesView, NewsListView, AdvicesListView, ArticleCreateView, \
    ArticleUpdateView, ArticleDeleteView, ArticleDetailView

urlpatterns = [
    path('', CommonArticlesView.as_view(), name='common articles views'),
    path('news/', NewsListView.as_view(), name='list news view'),
    path('advices/', AdvicesListView.as_view(), name='list advices view'),
    path('add/', ArticleCreateView.as_view(), name='add article view'),
    path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='edit article view'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete article view'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='detail article view'),
]