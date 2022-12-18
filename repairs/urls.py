from django.urls import path

from repairs.views import CreateRepair, ListRepair, DetailRepair, DeleteView

app_name = "repairs"

urlpatterns = [
    path('', ListRepair.as_view(), name="list"),
    path('create/', CreateRepair.as_view(), name="create"),
    path('detail/<int:pk>/', DetailRepair.as_view(), name="detail"),
    path('detail/<int:pk>/delete/', DeleteView.as_view(), name="delete"),
]
