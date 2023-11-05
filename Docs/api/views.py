from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import CustomUserSerializer, OrderSerializer, OrderItemSerializer, ProductSerializer
from .models import CustomUser, Order, OrderItem, Product
from rest_framework import status

@api_view(['GET'])
def home(request):
    data = {
        "urls": {
            "": reverse("home", request=request),
            "list-users": reverse("list-users", request=request),
            "get-users <id=int>": reverse("get-user", kwargs={'id':1}, request=request),
        }
    }
    return Response(data)

@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'success': False, 'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_user(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return Response({'success': False, 'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomUserSerializer(user)
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
    return Response({'success': False, 'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    


@api_view(['PUT'])
def update_user(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return Response({'success': False, 'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'success': False, 'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PATCH'])
def update_user_partial(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return Response({'success': False, 'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'success': False, 'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
def delete_user(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return Response({'success': False, 'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        user.delete()
        return Response({'success': True, 'message': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    return Response({'success': False, 'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def list_users(request):
    if request.method == 'GET':
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
    return Response({'success': False, 'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def advance_query(request):
    # Scenarion 1 : Only Staff Members
    # users = CustomUser.objects.filter(is_staff=True)
    # serializer = CustomUserSerializer(users, many=True)
    # return Response({'data':serializer.data})

    # Scenarion 2 : Joined after 2022
    # import datetime
    # users = CustomUser.objects.filter(date_joined__gte='2022-1-1')
    # serializer = CustomUserSerializer(users, many=True)
    # return Response({'data':serializer.data})

    # Scenarion 3 : Retrive products in a specific category
    products = Product.objects.filter(category = 1)
    serializer = ProductSerializer(products, many = True)
    return Response({'product':serializer.data})
