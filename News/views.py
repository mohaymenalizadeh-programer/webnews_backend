from rest_framework import viewsets, filters 
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Newsoftheday, NewsLifestyle, NewsDecoration, NewsTechnology, NewsArtculture, Slidertxt, Slidernews , Coment ,Visit, PageVideo , Portfolio
from .serializers import (
    NewsofthedaySerializer, NewsLifestyleSerializer,
    NewsDecorationSerializer, NewsTechnologySerializer,
    NewsArtcultureSerializer, SlidertextSerializer, 
    SlidernewsSerializer , ComentSerializer , 
    PortfolioSerializer
)


class NewsofthedayViewSet(viewsets.ModelViewSet):
    queryset = Newsoftheday.objects.all()
    serializer_class = NewsofthedaySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['txt_news', 'title_news', 'slug']
    lookup_field = 'slug'  

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.add_view()  # افزایش بازدید
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class NewsLifestyleViewSet(viewsets.ModelViewSet):
    queryset = NewsLifestyle.objects.all()
    serializer_class = NewsLifestyleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['begtxt', 'longtitle', 'slug']
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.add_view()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class NewsDecorationViewSet(viewsets.ModelViewSet):
    queryset = NewsDecoration.objects.all()
    serializer_class = NewsDecorationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['text', 'title', 'slug']
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.add_view()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class NewsTechnologyViewSet(viewsets.ModelViewSet):
    queryset = NewsTechnology.objects.all()
    serializer_class = NewsTechnologySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['matn', 'explanation', 'slug']
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.add_view()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class NewsSlidernewsViewSet(viewsets.ModelViewSet):
    queryset = Slidernews.objects.all()
    serializer_class = SlidernewsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category_tag', 'display_title', 'slug']
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.add_view()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class SliderstxtViewSet(viewsets.ModelViewSet):
    queryset = Slidertxt.objects.all()
    serializer_class = SlidertextSerializer


class NewsArtcultureViewSet(viewsets.ModelViewSet):
    queryset = NewsArtculture.objects.all()
    serializer_class = NewsArtcultureSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['dodslg', 'Artculture_title', 'slug']
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.add_view()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)










class NewsComentViewSet(viewsets.ModelViewSet):
    queryset = Coment.objects.all()
    serializer_class = ComentSerializer

    def get_queryset(self):
        queryset = Coment.objects.all()
        news_slug = self.request.query_params.get('slug')
        
        if self.action == 'list':
            queryset = queryset.filter(is_approved=True)
            if news_slug:
                queryset = queryset.filter(news_slug=news_slug)
                
        return queryset.order_by('-publish_date')




class ListApiview(APIView):
    def get(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
        device_type = 'Mobile' if ('mobile' in user_agent or 'android' in user_agent or 'iphone' in user_agent) else 'Desktop'
        Visit.objects.create(device=device_type)

        data = {
            "newsoftheday": list(Newsoftheday.objects.all().order_by('-publish_date')[:3].values(
                'txt_news', 'title_news', 'img_ftheday', 'slug', 'views', 'publish_date' , 'page_newsoftheday_title' , 'pagetxt_newsoftheday'
            )),
            "lifestyle": list(NewsLifestyle.objects.all().order_by('-publish_date')[:3].values(
                'begtxt', 'longtitle', 'img_Lifestyle', 'slug', 'views', 'publish_date', 'page_newsLifestyle_title', 'pagetxt_newsLifestyle'
            )),
            "decoration": list(NewsDecoration.objects.all().order_by('-publish_date')[:3].values(
                'text', 'title', 'img_Decoration', 'slug', 'views', 'publish_date' ,'page_newsDecoration_title','pagetxt_newsDecoration'
            )),
            "technology": list(NewsTechnology.objects.order_by('-publish_date')[2:5].values(
                'matn', 'explanation', 'img_Technology', 'slug', 'views', 'publish_date' , 'page_newsTechnology_title' , 'pagetxt_newsTechnology'
            )),
            "artculture": list(NewsArtculture.objects.all().order_by('-publish_date')[:3].values(
                'dodslg', 'Artculture_title', 'img_Artculture', 'slug', 'views', 'publish_date' , 'page_newsArtculture_title' , 'pagetxt_newsArtculture'
            )),
            "slidertxt": list(Slidertxt.objects.all().order_by('-text_slider')[:6].values(
                'text_slider'
            )),
            "latest_news_of_day": list(Newsoftheday.objects.all().order_by('-publish_date')[:3].values(
                'txt_news', 'title_news', 'img_ftheday', 'slug', 'views', 'publish_date' , 'page_newsoftheday_title' , 'pagetxt_newsoftheday'
            )),
            "latest_lifestyle": list(NewsLifestyle.objects.all().order_by('-publish_date')[:3].values(
                'begtxt', 'longtitle', 'img_Lifestyle', 'slug', 'views', 'publish_date', 'page_newsLifestyle_title', 'pagetxt_newsLifestyle'
            )),
            "latest_decoration": list(NewsDecoration.objects.all().order_by('-publish_date')[:3].values(
                'text', 'title', 'img_Decoration', 'slug', 'views', 'publish_date' ,'page_newsDecoration_title','pagetxt_newsDecoration'
            )),
            "latest_technology": list(NewsTechnology.objects.all().order_by('-publish_date')[:3].values(
                'matn', 'explanation', 'img_Technology', 'slug', 'views', 'publish_date' , 'page_newsTechnology_title' , 'pagetxt_newsTechnology'
            )),
            "latest_art_culture": list(NewsArtculture.objects.all().order_by('-publish_date')[:3].values(
                'dodslg', 'Artculture_title', 'img_Artculture', 'slug', 'views', 'publish_date' , 'page_newsArtculture_title' , 'pagetxt_newsArtculture'
            )),

            "finishtechnology_Last": NewsLifestyleSerializer(
                NewsLifestyle.objects.all().order_by('-publish_date')[:1],
                many=True,
                context={'request': request}
            ).data,

            "finishtechnology_Last_smallbox": NewsLifestyleSerializer(
                NewsLifestyle.objects.all().order_by('-publish_date')[1:4],
                many=True,
                context={'request': request}
            ).data,

            "ahsddecoration_Last": NewsDecorationSerializer(
                NewsDecoration.objects.all().order_by('-publish_date')[:1],
                many=True,
                context={'request': request}
            ).data,

            "ahsddecoration_Lastsmalltwos": NewsDecorationSerializer(
                NewsDecoration.objects.all().order_by('-publish_date')[1:4],
                many=True,
                context={'request': request}
            ).data,

            "artcultureslider": list(NewsArtculture.objects.all().order_by('-publish_date')[1:10].values(
                'dodslg', 'Artculture_title', 'img_Artculture', 'slug', 'views', 'publish_date', 
                'page_newsArtculture_title', 'pagetxt_newsArtculture'
            )),

            "allnewsofday": list(Newsoftheday.objects.all().order_by('-publish_date')[:60].values(
                'txt_news', 'title_news', 'img_ftheday', 'slug', 'views', 'publish_date' , 'page_newsoftheday_title' , 'pagetxt_newsoftheday'
            )),
            "alllifestyle": list(NewsLifestyle.objects.all().order_by('-publish_date')[:60].values(
                'begtxt', 'longtitle', 'img_Lifestyle', 'slug', 'views', 'publish_date', 'page_newsLifestyle_title', 'pagetxt_newsLifestyle'
            )),
            "alldecoration": list(NewsDecoration.objects.all().order_by('-publish_date')[:60].values(
                'text', 'title', 'img_Decoration', 'slug', 'views', 'publish_date' ,'page_newsDecoration_title','pagetxt_newsDecoration'
            )),
            "alltechnology": list(NewsTechnology.objects.all().order_by('-publish_date')[:60].values(
                'matn', 'explanation', 'img_Technology', 'slug', 'views', 'publish_date' , 'page_newsTechnology_title' , 'pagetxt_newsTechnology'
            )),
            "allartculture": list(NewsArtculture.objects.all().order_by('-publish_date')[:60].values(
                'dodslg', 'Artculture_title', 'img_Artculture', 'slug', 'views', 'publish_date' , 'page_newsArtculture_title' , 'pagetxt_newsArtculture'
            )),

            "twonewsofday": list(Newsoftheday.objects.all().order_by('-publish_date')[:2].values(
                'txt_news', 'title_news', 'img_ftheday', 'slug', 'views', 'publish_date' , 'page_newsoftheday_title' , 'pagetxt_newsoftheday'
            )),
            "twolifestyle": list(NewsLifestyle.objects.all().order_by('-publish_date')[:2].values(
                'begtxt', 'longtitle', 'img_Lifestyle', 'slug', 'views', 'publish_date', 'page_newsLifestyle_title', 'pagetxt_newsLifestyle'
            )),
            "twodecoration": list(NewsDecoration.objects.all().order_by('-publish_date')[:2].values(
                'text', 'title', 'img_Decoration', 'slug', 'views', 'publish_date' ,'page_newsDecoration_title','pagetxt_newsDecoration'
            )),
            "twotechnology": list(NewsTechnology.objects.all().order_by('-publish_date')[:2].values(
                'matn', 'explanation', 'img_Technology', 'slug', 'views', 'publish_date' , 'page_newsTechnology_title' , 'pagetxt_newsTechnology'
            )),
            "twoartculture": list(NewsArtculture.objects.all().order_by('-publish_date')[:2].values(
                'dodslg', 'Artculture_title', 'img_Artculture', 'slug', 'views', 'publish_date' , 'page_newsArtculture_title' , 'pagetxt_newsArtculture'
            )),

            "portfolio": list(Portfolio.objects.all()[:500].values(
                'text_portfolio', 'ttile_portfolio', 'img_portfolio', 'file_portfoli'
            )),

        }
        return Response(data)


class SingleNewsView(APIView):
    def get(self, request):
        data = {
            "newsoftheday": list(Newsoftheday.objects.all().order_by('-publish_date')[:1].values(
                'txt_news', 'title_news', 'img_ftheday', 'slug', 'views', 'publish_date' , 'page_newsoftheday_title' , 'pagetxt_newsoftheday'
            )),
            "lifestyle": list(NewsLifestyle.objects.all().order_by('-publish_date')[:1].values(
                'begtxt', 'longtitle', 'img_Lifestyle', 'slug', 'views', 'publish_date', 'page_newsLifestyle_title', 'pagetxt_newsLifestyle'
            )),
            "decoration": list(NewsDecoration.objects.all().order_by('-publish_date')[:1].values(
                'text', 'title', 'img_Decoration', 'slug', 'views', 'publish_date' ,'page_newsDecoration_title','pagetxt_newsDecoration'
            )),
            "technology": list(NewsTechnology.objects.all().order_by('-publish_date')[:1].values(
                'matn', 'explanation', 'img_Technology', 'slug', 'views', 'publish_date' , 'page_newsTechnology_title' , 'pagetxt_newsTechnology'
            )),
            "artculture": list(NewsArtculture.objects.all().order_by('-publish_date')[:1].values(
                'dodslg', 'Artculture_title', 'img_Artculture', 'slug', 'views', 'publish_date' , 'page_newsArtculture_title' , 'pagetxt_newsArtculture'
            )),
            "slidernews": list(Slidernews.objects.all().order_by('-publish_date')[:6].values(
                'category_tag', 'display_title', 'slider_image', 'slug', 'views', 'publish_date', 'Typenews'
            )),    
            "fordecoration": list(NewsDecoration.objects.all().order_by('-publish_date')[:4].values(
                'text', 'title', 'img_Decoration', 'slug', 'views', 'publish_date' ,'page_newsDecoration_title','pagetxt_newsDecoration'
            )), 
            "newsoftheday_archive": list(Newsoftheday.objects.all().order_by('-publish_date')[1:5].values(
                'txt_news', 'title_news', 'img_ftheday', 'slug', 'views', 'publish_date' , 'page_newsoftheday_title' , 'pagetxt_newsoftheday'
            )),
            "lifestyle_archive": list(NewsLifestyle.objects.all().order_by('-publish_date')[1:5].values(
                'begtxt', 'longtitle', 'img_Lifestyle', 'slug', 'views', 'publish_date', 'page_newsLifestyle_title', 'pagetxt_newsLifestyle'
            )),
            "decoration_archive": list(NewsDecoration.objects.all().order_by('-publish_date')[1:5].values(
                'text', 'title', 'img_Decoration', 'slug', 'views', 'publish_date' ,'page_newsDecoration_title','pagetxt_newsDecoration'
            )),
            "technology_archive": list(NewsTechnology.objects.all().order_by('-publish_date')[1:5].values(
                'matn', 'explanation', 'img_Technology', 'slug', 'views', 'publish_date' , 'page_newsTechnology_title' , 'pagetxt_newsTechnology'
            )),
            "artculture_archive": list(NewsArtculture.objects.all().order_by('-publish_date')[1:5].values(
                'dodslg', 'Artculture_title', 'img_Artculture', 'slug', 'views', 'publish_date' , 'page_newsArtculture_title' , 'pagetxt_newsArtculture'
            )),   
            "decorationfinish": list(NewsTechnology.objects.all().order_by('-publish_date')[:10].values(
                'matn', 'explanation', 'img_Technology', 'slug', 'views', 'publish_date' , 'page_newsTechnology_title' , 'pagetxt_newsTechnology'
            )),
            "technology_one": list(NewsTechnology.objects.all().order_by('-publish_date')[:1].values(
                'matn', 'explanation', 'img_Technology', 'slug', 'views', 'publish_date' , 'page_newsTechnology_title' , 'pagetxt_newsTechnology'
            )),

            "twonewsofdaysliders": list(Newsoftheday.objects.all().order_by('-publish_date')[:2].values(
                'txt_news', 'title_news', 'img_ftheday', 'slug', 'views', 'publish_date' , 'page_newsoftheday_title' , 'pagetxt_newsoftheday'
            )),
            "twolifestylesliders": list(NewsLifestyle.objects.all().order_by('-publish_date')[:2].values(
                'begtxt', 'longtitle', 'img_Lifestyle', 'slug', 'views', 'publish_date', 'page_newsLifestyle_title', 'pagetxt_newsLifestyle'
            )),
            "twodecorationsliders": list(NewsDecoration.objects.all().order_by('-publish_date')[:2].values(
                'text', 'title', 'img_Decoration', 'slug', 'views', 'publish_date' ,'page_newsDecoration_title','pagetxt_newsDecoration'
            )),
            "twotechnologysliders": list(NewsTechnology.objects.all().order_by('-publish_date')[:2].values(
                'matn', 'explanation', 'img_Technology', 'slug', 'views', 'publish_date' , 'page_newsTechnology_title' , 'pagetxt_newsTechnology'
            )),
            "twoartculturesliders": list(NewsArtculture.objects.all().order_by('-publish_date')[:2].values(
                'dodslg', 'Artculture_title', 'img_Artculture', 'slug', 'views', 'publish_date' , 'page_newsArtculture_title' , 'pagetxt_newsArtculture'
            )),
                
        }
        return Response(data)