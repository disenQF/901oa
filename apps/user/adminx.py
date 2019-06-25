import xadmin as admin
from xadmin.views import CommAdminView, BaseAdminView

from user.models import LoginUser, UserProfile
# Register your models here.

class GlobalSettings(object):
    # 整体配置
    site_title = 'xxx后台管理系统'
    site_footer = '西安千锋 Python1901'
    menu_style = 'accordion'  # 菜单折叠
    # 搜索模型
    global_search_models = [LoginUser]

    # 模型的图标(参考bootstrap图标插件)
    global_models_icon = {
        LoginUser: "glyphicon glyphicon-user"
    }  # 设置models的全局图标

    # 设置app模块的标题
    apps_label_title = {
        'user': '客户管理'
    }

    # 设置app模块的图标
    apps_icons = {
        'user': 'glyphicon glyphicon-user'
    }


class LoginUserAdmin():
    list_display = ['login_name', 'create_time', 'update_time']
    list_per_page = 20


class UserProfileAdmin():
    list_display = ['user', 'nick_name', 'real_name', 'card', 'phone']
    search_fields = ['nick_name', 'phone']
    list_per_page = 20


admin.site.register(CommAdminView, GlobalSettings)
admin.site.register(LoginUser, LoginUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)