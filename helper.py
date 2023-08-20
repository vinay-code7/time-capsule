from flask import session, redirect, url_for
from functools import wraps

def login_required(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        if 'username' in session:
            return view_func(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapped_view
