from django.urls import path
from .views import createUserView, loginView

urlpatterns = {
    path('signup/', createUserView.as_view(), name='signup'),
    path('login/', loginView.as_view(), name='login')
}
