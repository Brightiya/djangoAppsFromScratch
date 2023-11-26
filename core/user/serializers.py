from .models import User
from  ..abstract.serializers import AbstractSerializer


class UserSerializer(AbstractSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email',
                  'is_active', 'created', 'updated', 'bio', 'avatar']
        read_only_field = ['is_active']
