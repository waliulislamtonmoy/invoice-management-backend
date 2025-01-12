

from django.urls import path,include



from AppAccount.views import (
    UserRegisterView,
    SendOtpView,VeryfyOtpView,
    ResetPasswordView
)
    
    

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    
)

urlpatterns = [
    path('user-login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("user_registration/",UserRegisterView.as_view(),name='user_registration'),
    path("send-otp/",SendOtpView.as_view(),name="send-otp"),
    path("verify-otp/",VeryfyOtpView.as_view(),name="verify-otp"),
    path("reset-password/",ResetPasswordView.as_view(),name="reset-password"),
]
