from user.models import UserVideo
from django import forms
from user.widgets import VideoInput, VideoPosterInput


class UserVideoForm(forms.ModelForm):
    video_url = forms.CharField(label='视频', widget=VideoInput)
    video_poster = forms.CharField(label='封面', widget=VideoPosterInput)

    class Meta:
        model = UserVideo
        fields = "__all__"
