from django.contrib import admin

from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

import notifications.urls

from article.views import article_list
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # home
    path('', article_list, name='home'),
    # reset password app
    # path('password-reset/', include('password_reset.urls')),
    url(r'^password-reset/$', auth_views.PasswordResetView.as_view(
             template_name="passwordreset/password_reset_form.html",
             email_template_name="passwordreset/password_reset_email.html",
             subject_template_name="passwordreset/password_reset_subject.txt",
             success_url="/password-reset-done/"),
        name="password_reset"),
    url(r'^password-reset-done/$', auth_views.PasswordResetDoneView.as_view(template_name="passwordreset/password_reset_done.html"),
         name="password_reset_done"),
    url(r'^password-reset-confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.PasswordResetConfirmView.as_view(template_name="passwordreset/password_reset_confirm.html"),

         name="password_reset_confirm"),
    url(r'^password-reset-complete/$', auth_views.PasswordResetCompleteView.as_view(template_name="passwordreset/password_reset_complete.html"),
        name="password_reset_complete"),
    # set app's url
    path('article/', include('article.urls', namespace='article')),
    # userprofile
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
    # comment
    path('comment/', include('comment.urls', namespace='comment')),
    # djang-notifications
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    # notice
    path('notice/', include('notice.urls', namespace='notice')),
    # # django-allauth
    path('accounts/', include('allauth.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
