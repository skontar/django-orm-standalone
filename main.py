from db.models import Model

n = Model(number=1)
n.save()

print(Model.objects.all())