from rest_framework import serializers
from .models import Newsoftheday, NewsLifestyle, NewsDecoration, NewsTechnology , NewsArtculture , Slidertxt , Slidernews , Coment , Portfolio


class NewsofthedaySerializer(serializers.ModelSerializer):
    relative_time = serializers.CharField(source='get_relative_time', read_only=True)

    class Meta:
        model = Newsoftheday
        fields = '__all__'


class NewsLifestyleSerializer(serializers.ModelSerializer):
    relative_time = serializers.CharField(source='get_relative_time', read_only=True)

    class Meta:
        model = NewsLifestyle
        fields = '__all__'


class NewsDecorationSerializer(serializers.ModelSerializer):
    relative_time = serializers.CharField(source='get_relative_time', read_only=True)

    class Meta:
        model = NewsDecoration
        fields = '__all__'


class NewsTechnologySerializer(serializers.ModelSerializer):
    relative_time = serializers.CharField(source='get_relative_time', read_only=True)

    class Meta:
        model = NewsTechnology
        fields = '__all__'


class NewsArtcultureSerializer(serializers.ModelSerializer):
    relative_time = serializers.CharField(source='get_relative_time', read_only=True)

    class Meta:
        model = NewsArtculture
        fields = '__all__'     


class SlidertextSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slidertxt
        fields = '__all__'          



class SlidernewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slidernews
        fields = '__all__'          





class ComentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coment
        fields = '__all__'    





class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        fields = '__all__'           