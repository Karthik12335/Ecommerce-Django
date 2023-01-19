import factory

from ecommerce.product.models import Brand, Product, Category

class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Category
    name = factory.sequence(lambda n: "Category_%d" % n)

class BrandFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Brand
    name = factory.sequence(lambda n: "Brand_%d" % n)

class ProductFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Product

    name = "test_product"
    description = "test_description"
    is_digital = True
    is_active = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)