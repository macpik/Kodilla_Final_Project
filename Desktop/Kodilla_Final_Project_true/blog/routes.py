from flask import render_template, request
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm
from flask import render_template, request, flash, redirect, url_for


@app.route("/")
def index():
   return render_template("base.html")

@app.route("/homepage")
def show_homepage():
   all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())
   return render_template("homepage.html", all_posts=all_posts)

@app.route("/new-post/", methods=["GET", "POST"])
@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
def create_or_edit_entry(entry_id=None):
   if entry_id:
       entry = Entry.query.filter_by(id=entry_id).first_or_404()
       form = EntryForm(obj=entry)
   else:
       form = EntryForm()

   errors = None

   if request.method == 'POST':
       if form.validate_on_submit():
           if not entry_id:
               entry = Entry(
                   title=form.title.data,
                   body=form.body.data,
                   is_published=form.is_published.data
               )
               db.session.add(entry)
           else:
               form.populate_obj(entry)

           db.session.commit()
           flash('Done!', 'success')
           return redirect(url_for('show_homepage'))
       else:
           errors = form.errors

   return render_template("entry_form.html", form=form, errors=errors)