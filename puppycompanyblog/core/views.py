from flask import Flask, render_template, request, Blueprint
from puppycompanyblog.models import BlogPost, Photo
from puppycompanyblog.users.picture_handler import show_carousel_image


core = Blueprint('core', __name__)
# photos = Blueprint('photos', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page,per_page=2)
    return render_template('index.html', blog_posts=blog_posts)

@core.route('/info')
def info():
    photos = Photo.query.all()
    images = [show_carousel_image(photo.image) for photo in photos]
    # for photo in photos:
    #     show_carousel_image(photos)
    # selected_image = show_carousel_image()
    # image = url_for('static', filename='carousel/'+current_user.profile_image)
    return render_template('info.html', photos=photos, images=images)
