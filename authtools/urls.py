from django.conf.urls import url

from authtools import views


urlpatterns = [
    url(
        r'^$',
        views.LoginView.as_view(),
        name='login_small'
    ),
    url(
        r'^$',
        views.RegisterUserView.as_view(),
        name='register_small'
    ),

    url(
        r'^register/$',
        views.RegisterUserBigView.as_view(),
        name='register_big'
    ),

    url(
        r'^login/$',
        views.LoginBigView.as_view(),
        name='login_big'
    ),

    url(
        r'^logout/$'
        , views.LogoutView.as_view(),
        name='logout'
    ),
    url(
        r'^password_change/$',
        views.PasswordChangeView.as_view(),
        name='password_change'
    ),
    url(
        r'^password_change/done/$',
        views.PasswordChangeDoneView.as_view(),
        name='password_change_done'
    ),
    url(
        r'^password_reset/$',
        views.PasswordResetView.as_view(),
        name='password_reset'
    ),
    url(
        r'^password_reset/done/$',
        views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    url(
        r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    url(
        r'^reset/done/$',
        views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),


]