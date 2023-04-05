from userapi.viewsets import ClienteViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cliente', ClienteViewset)

#localhost:p/api/cliente
#GET, POST, UPDATE, DELETE
#list, read