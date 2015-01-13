#Snippet 1
#For deleting the duplicate entrys for a model

for row in MyModel.objects.all():
    if MyModel.objects.filter(photo_id=row.photo_id).count() > 1:
        row.delete()
        
#Snippet 2
#For getting the values out of a many-to-many-field in Django

model.entity.get_queryset()

#For adding the values

model.entity.add(value)
