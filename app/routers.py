from rest_framework.routers import DefaultRouter
from app.views import EmployeeViews

router = DefaultRouter()
router.register("employee",EmployeeViews,basename='yourmodel')