
from django.core.management.base import BaseCommand
from movies.models import Movie, Category, Cast
from datetime import datetime
import os

class Command(BaseCommand):
    help = 'Seed the database with initial movies data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Movie.objects.all().delete()
        Category.objects.all().delete()
        Cast.objects.all().delete()

        # Create categories
        action = Category.objects.create(name='Action')
        drama = Category.objects.create(name='Drama')

        # Create casts
        tom_hanks = Cast.objects.create(name='Tom Hanks')
        meryl_streep = Cast.objects.create(name='Meryl Streep')

        # Define the media directory
        media_dir = os.path.join('media', 'posters')

        # Ensure the directory exists
        os.makedirs(media_dir, exist_ok=True)

        # Create movies
        movie1 = Movie.objects.create(
            title='Saving Private Ryan',
            description='A group of soldiers go behind enemy lines to retrieve a paratrooper whose brothers have been killed in action.',
            release_date=datetime.strptime('1998-07-24', '%Y-%m-%d'),
            poster_image=os.path.join(media_dir, 'saving_private_ryan.jpg')
        )
        movie1.categories.set([action, drama])
        movie1.casts.set([tom_hanks])

        movie2 = Movie.objects.create(
            title='The Post',
            description='A cover-up that spanned four U.S. Presidents pushed the country\'s first female newspaper publisher and a hard-driving editor to join an unprecedented battle between journalist and government.',
            release_date=datetime.strptime('2017-12-22', '%Y-%m-%d'),
            poster_image=os.path.join(media_dir, 'the_post.jpg')
        )
        movie2.categories.set([drama])
        movie2.casts.set([tom_hanks, meryl_streep])

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with movies'))
