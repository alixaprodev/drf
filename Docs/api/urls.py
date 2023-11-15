from django.urls import path
from . import views


urlpatterns=[
    path('', views.home, name='home'),
    
    # path('users/',views.create_user, name='create-user'),
    # path('users/',views.list_users, name='list-users'),
    # path('users/<int:id>',views.update_user, name='update-user'),
    # path('users/<int:id>',views.update_user_partial, name='update-user-partial'),
    # path('users/<int:id>',views.delete_user, name='delete-user'),

    path('users/create', views.create_user, name='create-user'),

    # Get a user by ID using GET
    path('users/<int:user_id>/', views.get_user, name='get-user'),

    # Update a user by ID using PUT
    path('users/<int:user_id>/update', views.update_user, name='update-user'),

    # Partially update a user by user_id using PATCH
    path('users/<int:user_id>/partial/', views.update_user_partial, name='update-user-partial'),

    # Delete a user by user_id using DELETE
    path('users/<int:user_id>/delete/', views.delete_user, name='delete-user'),

    # List all users using GET
    path('users/', views.list_users, name='list-users'),

    # Advance Queries
    path('advance-query/<str:int_param>/',views.advance_query, name='advance-query')
]
