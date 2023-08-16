from rest_framework import serializers
from django.db.models import Avg

from apps.second_assignment.models import Product, Company, Comment


class ProductSerializer(serializers.ModelSerializer):
    discount_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'company',
            'name',
            'price',
            'discount',
            'discount_price'
        )

    def get_discount_price(self, instance):
        if instance.discount > 0:
            price = instance.price
            discount_price = (instance.discount / 100) * price
            return int(discount_price)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'user',
            'company',
            'rating',
            'message'
        )


class CompanyProductsSerializer(serializers.ModelSerializer):
    company_product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = (
            'name',
            'image',
            'company_product',
        )


class CompanyCommentSerializer(serializers.ModelSerializer):
    company_comment = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField(read_only=True)
    avg_rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Company
        fields = (
            'comment_count',
            'avg_rating',
            'name',
            'image',
            'company_comment',
        )

    def get_comment_count(self, obj):
        return obj.company_comment.count()

    def get_avg_rating(self, obj):
        return 123

    # def get_avg_rating(self, obj):
    #     company_id = self.context.get("company_id")
    #
    #     company_rating_avg = Comment.objects.filter(
    #         company_comment=company_id,
    #     ).aggregate(video_count=Avg("rating"))["rating_avg"]
    #     return int(company_rating_avg)
