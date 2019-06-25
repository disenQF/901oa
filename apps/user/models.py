from django.contrib.auth.hashers import make_password
from django.db import models



# Create your models here.
class LoginUser(models.Model):
    login_name = models.CharField(max_length=20,
                                  verbose_name='账号名')
    login_auth_str = models.CharField(max_length=200,
                                      verbose_name='口令')
    create_time = models.DateTimeField(verbose_name='注册时间',
                                       auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间',
                                       auto_now=True)
    note = models.CharField(max_length=50,
                            blank=True,
                            null=True)

    def __str__(self):
        return self.login_name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if all((len(self.login_auth_str) < 70,
                not self.login_auth_str.startswith('pbkdf2_sha256$36000$'))):
            self.login_auth_str = make_password(self.login_auth_str)
        super().save()


    class Meta:
        db_table = 'app_user_2'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

