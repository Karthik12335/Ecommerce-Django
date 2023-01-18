import pytest

pytestmark = pytest.mark.django_db

class TestCategoryModel:
    def test_str_method(self, category_factory):
        #arrange
        #act
        x = category_factory(name = "test_category")
        
        #assert
        assert x.__str__() == "test_category"

class TestProductModel:
    def test_str_method(self, product_factory):
        #arrange
        #act
        x = product_factory(name="test_product")
        #assert
        assert x.__str__() == "test_product"

class TestBrandModel:
    def test_str_method(self, brand_factory):
        #arrange
        #act
        x = brand_factory(name="test_brand")
        #assert
        assert x.__str__() == "test_brand"