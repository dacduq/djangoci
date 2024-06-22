import factory

class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'blogs.Blog'

    title = factory.Faker('sentence', nb_words=4)
    subtitle = factory.Faker('sentence', nb_words=6)
    content = factory.Faker('paragraph', nb_sentences=4)