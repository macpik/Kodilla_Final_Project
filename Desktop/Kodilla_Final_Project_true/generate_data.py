from faker import Faker
from blog.models import Entry, db
from blog import app

def generate_entries(how_many=10):
    fake = Faker()

    with app.app_context():
        for i in range(how_many):
            post = Entry(
                title=fake.sentence(),
                body='\n'.join(fake.paragraphs(15)),
                is_published=True
            )
            db.session.add(post)
        db.session.commit()

if __name__ == "__main__":
    generate_entries()
