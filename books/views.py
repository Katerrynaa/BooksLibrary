from .models import Books
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import BooksSerializer, RatingSerializer, PriceSerializer, WeeklySerializer

from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView



class BooksApiListPagination(PageNumberPagination):
    page_size = 7
    page_query_param = 'page_size'
    max_page_size = 500


class BooksApiView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    pagination_class = BooksApiListPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genre']
    # permission_classes = ( IsAuthenticated, )


class BookPostApiView(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    # permission_classes = (IsAuthenticated, )


class BookUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    # permission_classes = (IsAdminUser, )


class BookDeleteApiView(generics.RetrieveDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    # permission_classes = (IsAdminUser, )


class ThrottleView(APIView):
    throttle_classes = [UserRateThrottle]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
    

class RatingView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = RatingSerializer
    pagination_class = BooksApiListPagination
    # permission_classes = (IsAuthenticated, )


class PriceView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = PriceSerializer
    pagination_class = BooksApiListPagination
    # permission_classes = (IsAuthenticated, )


class WeeklyRecommendationView(generics.ListAPIView):
    serializer_class = WeeklySerializer
    # permission_classes = (IsAuthenticated, )

    def get_queryset(self):
         return [Books.objects.get(pk=73)]