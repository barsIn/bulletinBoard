from .views import AdvertisementView, AdvertisementDetailView, AdvCreate, AdvUpdate, AdvDeleteView, respCreate, UserDetailView, confirm_resp, delete_resp
from django.urls import path

urlpatterns = [
    path('', AdvertisementView.as_view(), name='index'),
    path('adv/<int:pk>/', (AdvertisementDetailView.as_view()), name='adv_detail'),
    path('create/', AdvCreate.as_view(), name='create'),
    path('resp/create/<int:pk>', respCreate, name='createresp'),
    path('<int:pk>/delete/', AdvDeleteView.as_view(), name='adv_delete'),
    path('update/<int:pk>/', AdvUpdate.as_view(), name='adv_update'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='userinfo'),
    path('resp/confirm/<int:id>/', confirm_resp, name='confirm_resp'),
    path('resp/delete/<int:id>/', delete_resp, name='delete_resp'),

]