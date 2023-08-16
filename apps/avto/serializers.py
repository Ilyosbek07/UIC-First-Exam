from rest_framework import serializers

from apps.avto.models import Announcement

choice = (
    ('Cheap price', 'Cheap price'),
    ('Good price', 'Good price'),
    ('cheap price', 'cheap price')
)


class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'
