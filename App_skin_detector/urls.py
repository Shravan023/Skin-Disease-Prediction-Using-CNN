from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
				path('',views.Home,name="Home"),
				path('Upload_image/',views.Upload_image,name="Upload_image"),
				path('View_doctors/',views.View_doctors,name="View_doctors"),
				path('register/',views.Register,name="register"),
				path('login/',views.login,name="login"),
				path('Admin_Login/',views.Admin_Login,name="Admin_Login"),
				path('Logout/',views.Logout,name="Logout"),
				path('feedback/',views.feedback,name="feedback"),
				path('View_feedback/',views.View_feedback,name="View_feedback"),
				path('View_doctors/',views.View_doctors,name='View_doctors'),
				path('Update_Doctor/',views.Update_Doctor,name="Update_Doctor"),
				path('Add_Doctor/',views.Add_Doctor,name="Add_Doctor"),
				path('View_Doctors2/',views.View_Doctors2,name='View_Doctors2'),
				path('delete_doctor/<int:id>', views.delete_doctor, name='delete_doctor'),
				path('View_Users/',views.View_Users,name="View_Users"),
				path('Add_Medicine/',views.Add_Medicine,name="Add_Medicine"),
				path('manage_medicine/',views.manage_medicine,name='manage_medicine'),
				path('View_Medicine/',views.View_Medicine,name='View_Medicine'),
				path('Update_Medicine/',views.Update_Medicine,name='Update_Medicine'),
				path('delete_medicine/<int:id>',views.delete_medicine,name='delete_medicine'),
				path('Medicine/',views.Medicine,name='Medicine'),
				path('View_Doctors_New/<str:detected>',views.View_Doctors_New,name='View_Doctors_New'),




]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 