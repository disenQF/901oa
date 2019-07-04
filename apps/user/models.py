from oa_v1.helper import make_password
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
    activated = models.IntegerField(verbose_name='是否激活', choices=((0, '未激活'), (1, '已激活')), default=0)
    note = models.CharField(max_length=50,
                            blank=True,
                            null=True)

    def __str__(self):
        return self.login_name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if len(self.login_auth_str) < 32:
            self.login_auth_str = make_password(self.login_auth_str)
        super().save()

    class Meta:
        db_table = 'app_user_2'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


class UserProfile(models.Model):
    user = models.ForeignKey(LoginUser,
                                verbose_name='用户ID',
                                on_delete=models.CASCADE)

    nick_name = models.CharField(max_length=20, verbose_name='昵称', null=True, blank=True)
    phone = models.CharField(max_length=15, verbose_name='手机号', null=True, blank=True)
    photo = models.ImageField(verbose_name='用户头像',
                              upload_to='users/photo', null=True, blank=True)

    real_name = models.CharField(max_length=20, verbose_name='真实姓名', null=True, blank=True)
    image_forward = models.ImageField(verbose_name='身份正面照片', upload_to='users/photo',null=True, blank=True)
    image_back = models.ImageField(verbose_name='身份反面照片', upload_to='users/photo',null=True, blank=True)
    card = models.CharField(max_length=20, verbose_name='身份证号码', null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        # 删除文件
        super().delete()

    def __str__(self):
        return self.user.login_name

    class Meta:
        db_table = 'app_user_profile'
        verbose_name = '用户详情'
        verbose_name_plural = verbose_name


class UserVideo(models.Model):
    user = models.ForeignKey(LoginUser,
                             verbose_name='用户名',
                             on_delete=models.CASCADE)

    video_url = models.CharField(max_length=200,
                                 verbose_name='视频下载')
    title = models.CharField(max_length=200, verbose_name='视频标题')
    content = models.TextField(verbose_name='内容简介', blank=True, null=True, max_length=400)
    video_poster = models.CharField(max_length=100, verbose_name='视频封面图片', blank=True, null=True)

    def __str__(self):
        return self.user.login_name

    class Meta:
        db_table = 'app_user_video'
        verbose_name = '用户视频'
        verbose_name_plural = verbose_name
