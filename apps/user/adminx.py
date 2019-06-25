import xadmin as admin


from user.models import LoginUser
from user.forms import LoginUserForm
# Register your models here.

class LoginUserAdmin():
    form = LoginUserForm
    list_display = ['login_name', 'create_time', 'update_time']
    list_per_page = 20


admin.site.register(LoginUser, LoginUserAdmin)