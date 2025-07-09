from django.urls import path

from .views import ProductListView, ProductDetailView, CategoryListView, CategoryDetailView, FileListView, FileDetailView


urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),

    path('products/<int:product_id>/files/', FileListView.as_view(), name='files-list'),
    path('products/<int:product_id>/files/<int:id>/', FileDetailView.as_view(), name='files-detail'),
]