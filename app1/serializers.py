from rest_framework import serializers
from .models import *


class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class ObunaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Obuna
        fields = "__all__"


class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class PleylistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pleylist
        fields = "__all__"


class HistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"

