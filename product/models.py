from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('common.Category', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='product_images')

    def __str__(self):
        return f"{self.product} - {self.image}"


class AttributeName(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='attribute_names')

    def __str__(self):
        return f"{self.product} - {self.name}"


class AttributeValue(models.Model):
    title = models.CharField(max_length=255, null=True)
    value = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    attribute_name = models.ForeignKey('product.AttributeName', on_delete=models.CASCADE,
                                       related_name='attribute_values')

    def __str__(self):
        return f"{self.attribute_name} - {self.title}"
