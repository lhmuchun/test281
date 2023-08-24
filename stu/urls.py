from django.conf.urls import url
import views


urlpatterns = [
    url(r"^$", views.AreaView.as_view()),
    url(r"^getInfo/$", views.getInfo),
]