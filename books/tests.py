from rest_framework.test import APITestCase
from rest_framework import status
from .models import Books, Genre

class MyBooksGetApiTest(APITestCase):
    def setUp(self):
        genre = Genre.objects.create(name='name')
        Books.objects.create(author='author', title='title', description='description',
                             year='1883', country='country', genre=genre, price='price')
        
    
    def test_get_data(self):
        url = '/api/v1/books/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MyBooksPostApiTest(APITestCase):
    def test_post_data(self):
        genre = Genre.objects.create(name='name')
        url = '/api/v1/books/create/'
        data = {
            'author': 'author',
            'title': 'title',
            'description': 'description',
            'year': '1883',
            'country': 'country',
            'genre': genre.id,
            'price': 'price'
        }
        resposnse = self.client.post(url, data=data)
        self.assertEqual(resposnse.status_code, status.HTTP_201_CREATED)



class MyBookDeleteApiTest(APITestCase):
    def setUp(self):
        genre = Genre.objects.create(name='name')
        self.book = Books.objects.create(
            author='Walter Isaacson',
            title='Steve Jobs',
            description='Biography of the creation and influence of Steve Jobs on the technological world',
            year='2011',
            country='United States',
            genre=genre,
            price='63$'
    
        )

    def test_delete_book(self):
        url = f'/api/v1/books/delete/{self.book.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Books.objects.filter(id=self.book.id).exists())


