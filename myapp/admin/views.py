from myapp.admin import admin


@admin.route('/')
def index():
    return '<h1>Hello Admin!</h1>'
