from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
class ResgisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'password2', 'nickname', 'location', 'university']