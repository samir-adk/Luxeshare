from restframework import serializers
from Car.models import CarCategory,Vehicle

class CarCategorySerializers(serializers.ModelSeializer):
	class Meta:
		fields='__all__'
		model=CarCategory

class CarListSerializer(serializers.ModelSeializer):
	class Meta:
		fields='__all__'
		model=Vehicle