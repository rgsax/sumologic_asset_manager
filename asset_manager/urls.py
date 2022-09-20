from django.urls import path

from . import views

app_name = 'asset_manager'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('asset/<str:asset>', views.AssetView.as_view(), name='assets'),
    path('instances/', views.get_instances, name='assets'),
    path('manage/create/', views.create_instance, name='create_instance'),
    path('manage/instance/', views.InstanceView.as_view(), name='manage'),
    path('manage/instance/<str:tag>', views.InstanceView.as_view(), name='delete_asset')
]