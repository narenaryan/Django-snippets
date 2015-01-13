#Snippet 1
#For deleting the duplicate entrys for a model

for row in MyModel.objects.all():
    if MyModel.objects.filter(photo_id=row.photo_id).count() > 1:
        row.delete()
        
#Snippet 2
