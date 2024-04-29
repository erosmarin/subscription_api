from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
industry_choices = (('consumer_health', 'Consumer Health'),
                    ('beauty', 'Beauty'),
                    ('tech', 'Tech'))
source_choices = (('social_media', 'Social Media'),
                  ('news', 'News'))
subcategory_choices = (('new_product_releases', 'New Product Releases'),
                       ('mergers_acquisitions', 'Mergers & Acquisitions'))
class Subscriber (models.Model):
    email = models.EmailField(null=False)
    date = models.DateTimeField(auto_now_add=True)
    industry = MultiSelectField(null=True,
                                choices=industry_choices, 
                                max_length=100)
    source = MultiSelectField(null=True,
                              choices=source_choices,
                              max_length=100)
    subcategory = MultiSelectField(null=True,
                              choices=subcategory_choices,
                              max_length=100)
