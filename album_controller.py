import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to
from albums.lib.widgets import NiceForm
import tw.forms as twf

from albums.lib.base import BaseController, render
from albums.lib.identity_session import expire_session, require_user

from albums.model import album

add_album_form = NiceForm('add_albums', method='post', action='perform_add_album', children=[
    twf.TextField('name', validator=twf.validators.String(not_empty=True)),
    twf.CheckBox('public', help_text="Check this box if you would like your album to be publicly visible")
], submit_text="Save")

class AlbumController(BaseController):
    @require_user
    def add_album(self):
        c.form = add_album_form
        return render('/add_album.mako')
    
    @validate(form=add_album_form, error_handler="add_album")
    @require_user
    def perform_add_album(self):
        r = self.form_result
        album.add_album(c.real_identity.username, r.get('name'), r.get('public'), c.identity.username)
        redirect_to(controller="user", action="dashboard")
        