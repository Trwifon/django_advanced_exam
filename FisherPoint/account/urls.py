from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from FisherPoint.account.views import UserRegisterView, UserDetailsView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/', include([
        path('details/', UserDetailsView.as_view(), name='profile_details'),
        path('update/', UserUpdateView.as_view(), name='profile_update'),
        path('delete/', UserDeleteView.as_view(), name='profile_delete'),
    ]))
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)