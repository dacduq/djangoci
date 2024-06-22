from django.test import TestCase
from django.urls import reverse
from . import models as blog_models
from .factory import BlogFactory

class BlogTestCase(TestCase):
    def setUp(self):
        for i in range(12):
            BlogFactory()

    def test_blog_list(self):
        response = self.client.get(reverse("blog_index"))
        blog_list = blog_models.Blog.objects.all()[:10]
        response_list = response.context["blog_list"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(blog_list), len(response_list))
        
        for i, blog in enumerate(blog_list):
            self.assertEqual(blog.id, response_list[i].id)