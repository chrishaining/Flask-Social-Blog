from puppycompanyblog import db
from puppycompanyblog.models import Photo

Photo.query.delete()

photo1 = Photo(image='pup1.png', title='Puppy 1')


db.session.add(photo1)

db.session.commit()

print(photo1.title)
print(photo1)
print(photo1.image)
