import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album import Album
from lib.artist import Artist
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/goodbye')
def get_goodbye():
    return render_template('goodbye.html', farewell='Bye!')


# == Artist / Album Routes ==
@app.route('/artists')
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    return "\n".join(
        f"{artist}" for artist in repository.all()
    )

@app.route('/artists', methods=["POST"])
def post_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(
        None,
        request.form["name"],
        request.form["genre"],
    )
    repository.create(artist)
    return '', 200

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    # return "\n".join(
    #     f"{album}" for album in repository.all()
    # )
    return render_template('albums.html', albums=albums)

@app.route('/albums', methods=['POST'])
def post_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(
        None,
        request.form['title'],
        request.form['release_year'],
        request.form['artist_id'],
    )
    repository.create(album)
    return '', 200

# using path variable i.e. /albums/<id>
@app.route('/albums/<id>')
def get_album_by_id(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    return render_template('album.html', album=album)

# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji='^_^')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
