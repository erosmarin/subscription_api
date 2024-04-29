from .models import Subscriber, industry_choices, source_choices, subcategory_choices
from rest_framework import fields, serializers

class SubscriberSerializer(serializers.HyperlinkedModelSerializer):
    industry    = fields.MultipleChoiceField(choices=industry_choices)
    source      = fields.MultipleChoiceField(choices=source_choices)
    subcategory = fields.MultipleChoiceField(choices=subcategory_choices)
    class Meta:
        model = Subscriber
        fields = ['email', 'date', 'industry', 'source', 'subcategory']