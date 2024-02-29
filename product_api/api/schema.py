import graphene

from graphene_django import DjangoObjectType, DjangoListField
from .models import Product, Store

class StoreType(DjangoObjectType):
    class Meta:
        model = Store
        fields = "__all__"

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"
    
    store = graphene.Field(StoreType)

    def resolve_store(self, info):
        return self.store

class Query(graphene.ObjectType):
    all_store = graphene.List(StoreType)
    store = graphene.Field(StoreType, store_id=graphene.Int())

    all_products = graphene.List(ProductType)
    product = graphene.Field(ProductType, product_id=graphene.Int())

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_product(self, info, product_id):
        return Product.objects.get(pk=product_id)
    
    def resolve_all_store(self, info, **kwargs):
        return Store.objects.all()

    def resolve_store(self, info, store_id):
        return Store.objects.get(pk=store_id)
    
schema = graphene.Schema(query=Query)