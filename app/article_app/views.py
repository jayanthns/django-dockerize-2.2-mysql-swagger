from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from common.util.response import return_error_response
from common.util.logger import get_custom_logger

from .models import Article
from .serializers import ArticleSerializer

log = get_custom_logger()
articles_response = openapi.Response('response description', ArticleSerializer)

# Create your views here.


@swagger_auto_schema(methods=['get'], responses={200: articles_response})
@swagger_auto_schema(methods=['post'], request_body=ArticleSerializer)
@api_view(['GET', 'POST'])
def articles_api_view(request):
    """
    Create an Article or get all articles
    """

    log.info("WORKING")
    # Getting all articles
    if request.method == 'GET':
        article_queryset = Article.objects.all()
        serializer = ArticleSerializer(article_queryset, many=True)
        return Response(
            {
                "data": serializer.data,
                "status": 200,
                "code": 200,
                "message": "Articles fetched successfully."
            },
            status=status.HTTP_200_OK
        )

    # Creating an new article
    request_data = request.data
    serializer = ArticleSerializer(data=request_data)
    if not serializer.is_valid():
        return return_error_response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return Response(
        {
            "data": serializer.data,
            "code": 201,
            "status": 201,
            "message": "Article created successfully."
        },
        status=status.HTTP_201_CREATED
    )


@swagger_auto_schema(methods=['delete'], responses={200: "article deleted response"})
@swagger_auto_schema(methods=['get'], responses={200: articles_response})
@swagger_auto_schema(methods=['put'], request_body=ArticleSerializer)
@api_view(['GET', 'DELETE', 'PUT'])
def article_update_delete_api_view(request, pk):
    """
    Update an Article or Delete an Article by id
    """

    # Finding an article by id.
    try:
        article = Article.objects.get(id=pk)
    except Article.DoesNotExist:
        return return_error_response(F"Article with the id {pk} does not exist.", 404)
    except Exception as e:
        log.error(e)
        return return_error_response(
            "Something went wrong. Please try again later.", 400
        )

    # Get the article details
    if request.method == "GET":
        return Response(
            {
                "data": ArticleSerializer(article).data,
                "code": 200,
                "status": 200,
                "message": "Article updated successfully."
            },
            status=status.HTTP_200_OK
        )

    # Delete an article
    if request.method == 'DELETE':
        article.delete()
        return Response(
            {
                "message": "Article deleted successfully.",
                "code": 200,
                "status": 200,
                "data": None
            },
            status=status.HTTP_200_OK
        )

    # Update an article by id
    serializer = ArticleSerializer(article, data=request.data)
    if not serializer.is_valid():
        return return_error_response(serializer.errors, 400)
    serializer.save()
    return Response(
        {
            "data": serializer.data,
            "code": 200,
            "status": 200,
            "message": "Article updated successfully."
        },
        status=status.HTTP_200_OK
    )
