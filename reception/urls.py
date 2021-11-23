from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path
from django.urls import reverse_lazy
from . import views


app_name = 'reception'
urlpatterns = [
    path('', views.all_tutors, name='all_tutor'),
    path('<slug:slug>', views.create_reception, name='create_reception'),
    path('create_feedback/<slug:slug>', views.create_feedback, name='create_feedback'),
    path('see_feedback/<slug:slug>', views.see_feedback, name='see_feedback'),
    path('registration/', views.registration, name='registration'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('edit_user_profile/', views.edit_user_profile, name='edit_user_profile'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy('reception:password_reset_done'),
    ), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('reception:password_reset_complete'),
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
