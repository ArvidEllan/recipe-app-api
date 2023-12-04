

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model 
User = get_user_model()



class ModelTest(TestCase):
    

    def test_create_user_with_email_successful(self,username):
        """Test creating a new user with an email is successful"""
        email='test@example.com'
        password='testpass2331'
        user= get_user_model().objects.create_user(
            email=email,
            password=password,
    
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
        
    def test_new_user_email_normaized(self ):

        def test_create_user_with_email_successful(self):
            """Test creating a new user with an email is successful"""
        # email='test@example.com'
        # password='testpass2331'
            self.user= User.objects.create_user(
                email='test@example.com',
                password='testpass124',
                username = 'testname '
        
            )
            self.assertEqual(self.user.email,'test@example.com')
            self.assertTrue(self.user.check_password(password))

        def test_new_user_email_normalized(self ):

            sample_emails = [
                ['test1@example.com', 'test1@example.com'],
                ['Test2@example.com', 'test2@example.com'],
                ['TEST3@EXAMPLE.COM', 'test3@example.com'],
                
            ]
            for email , expected in sample_emails:

                user = get_user_model().objects.create_user(email, 'sample123')
                self.assertEqual(user,email,expected)
                

                user = User.objects.create_user(email, 'sample123',)
                
                self.assertEqual(user,email,expected)
            
            
         

    def test_new_user_without_email_raises_error(self):
        '''Test that creating user without email raises error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test1234567890')
    

    def test_create_new_superuser(self,username ):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@londonappdev.com',
            'test123')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@londonappdev.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

