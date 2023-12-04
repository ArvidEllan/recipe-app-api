#test for user api
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')

def create_user(**params):
    
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the users API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""
        payload = {
            'email':'test1@example.com',
            'password':'changeme1234',
            'name':'Test name'
        }
        res = self.client.post(CREATE_USER_URL,payload)

        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password',res.data)


    def test_user_exists(self):
        """Test creating a user that already exists fails"""
        payload = {
            'email':'test2@example.com',
            'password':'testpasschange1234',
            'name':'Test name'
        }
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL,payload)

        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter()
        
    def test_password_too_short_error(self):
        """Test that the password must be more than 5 characters"""
        payload = {
            'email':'test3@example.com',
            'password':'testpass98664chnage',
            'name':'Test name'
        }
        res = self.client.post(CREATE_USER_URL,payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exist = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exist)
    
    def test_create_token_for_user(self):
        user_details = {
            'email':'test4@example.com',
            'password':'<PASSWORD>',
            'name': 'Test name',
            }
        create_user(**user_details)
        payload = {
            'email':user_details['email'],
            'password': user_details['password'],
        }
        res = self.client.post(TOKEN_URL,payload)
        
        self.assertIn('token',res.data)
        self.assertEqual(res.status_code,status.HTTP_200_OK)
    
    def test_create_token_bad_credential(self):
        """Test that token is not created if invalid credentials are given"""
        create_user(email='test5@example.com',password='goodpass')
        payload = {
            'email':'test5@example.com',
            'password':'badpass',
        }
        res = self.client.post(TOKEN_URL,payload)

        self.assertNotIn('token',res.data)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
        
    def test_create_token_blank_password(self):
        """Test that token is not created if password is blank"""
        create_user(email='test6@example.com',password='test123change')
        payload = {
            'email':'test6@example.com',
            'password':'',
        }
        res = self.client.post(TOKEN_URL,payload)
        self.assertNotIn('token',res.data)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
        