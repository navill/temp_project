from rest_framework import serializers

from accounts.models import User
from product.models import Category, Product, Comment


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)

    class Meta:
        model = Category
        fields = ['url', 'id', 'name', 'products']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.SlugRelatedField(queryset=Product.objects.all(), slug_field='name')
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ['id', 'user', 'product', 'reply', 'body']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'description', 'price', 'quantity', 'created', 'comments']
