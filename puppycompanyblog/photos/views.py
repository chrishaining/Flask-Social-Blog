# from flask import render_template, url_for, flash, request, redirect, Blueprint
# from flask_login import current_user, login_required
# from puppycompanyblog import db
# from puppycompanyblog.models import Photo
#
# photos = Blueprint('photos', __name__)
#
#
# ########################
# ### view all photos ###
# ########################
# @photos.route('/')
# def blog_post(blog_post_id):
#     photos = Photo.query.all()
#     blog_post = BlogPost.query.get_or_404(blog_post_id)
#     return render_template('info.html', photos=photos)
#
#
# ##############
# ### update ###
# ##############
# @blog_posts.route('/<int:blog_post_id>/update', methods=['GET', 'POST'])
# @login_required
# def update(blog_post_id):
#
#     blog_post = BlogPost.query.get_or_404(blog_post_id)
#
#     if blog_post.author != current_user:
#         abort(403)
#
#     form = BlogPostForm()
#
#     if form.validate_on_submit():
#         blog_post.title = form.title.data
#         blog_post.text=form.text.data
#         db.session.commit()
#         flash('Blog post updated')
#         return redirect(url_for('blog_posts.blog_post', blog_post_id=blog_post.id))
#
#     elif request.method == 'GET':
#         form.title.data = blog_post.title
#         form.text.data = blog_post.text
#
#     return render_template('create_post.html', form=form)
#
# ##############
# ### delete ###
# ##############
# @blog_posts.route('/<int:blog_post_id>/delete', methods=['GET', 'POST'])
# @login_required
# def delete_post(blog_post_id):
#
#     blog_post = BlogPost.query.get_or_404(blog_post_id)
#
#     if blog_post.author != current_user:
#         abort(403)
#
#     db.session.delete(blog_post)
#     db.session.commit()
#     flash('Blogpost deleted')
#     return redirect(url_for('core.index'))
