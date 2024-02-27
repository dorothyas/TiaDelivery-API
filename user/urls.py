from django.urls import path
from .views import MyTokenObtainPairView, RegisterView
from user import views
from allauth.socialaccount.views import signup
from user.views import GoogleLogin 

urlpatterns = [
#Authentication
path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
# path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
path('register/', RegisterView.as_view(), name='auth_register'),

#Profile
path('profile/', views.getProfile, name='profile'),
path('profile/update/', views.updateProfile, name='update-profile'),

path('signup', signup, name="socialaccount_signup"),
path('google/', GoogleLogin.as_view(), name='google_login')
]