<%inherit file="/base.mako" />

<%def name="title_tags()">
Add Album
</%def>
<p>
  Create a new album.
</p>
${ c.form(value=c.value) | n }
