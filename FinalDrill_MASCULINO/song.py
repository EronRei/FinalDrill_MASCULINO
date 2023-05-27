from flask import Flask, request, jsonify, abort

app = Flask(__name__)

songs = [
    {
        'Title': 'Rise Up',
        'Artist': 'Andra Day',
        'Genre': 'Pop',
        'ID': 123123,
        'Release': 2016
    },
    {
        'Title': 'Bohemian Rhapsody',
        'Artist': 'Queen',
        'Genre': 'Rock',
        'ID': 123124,
        'Release': 1975
    },
    {
        'Title': 'Blinding Lights',
        'Artist': 'The Weeknd',
        'Genre': 'Pop',
        'ID': 123125,
        'Release': 2019
    },
    {
        'Title': 'Shape of You',
        'Artist': 'Ed Sheeran',
        'Genre': 'Pop',
        'ID': 123126,
        'Release': 2017
    },    
    {
        'Title': 'Can\'t Stop the Feeling!',
        'Artist': 'Justin Timberlake',
        'Genre': 'Pop',
        'ID': 123127,
        'Release': 2016
    }
]

@app.route("/songs", methods=['GET'])
def get_songs():
    return jsonify({'songs': songs})

@app.route("/songs/<int:ID>", methods=['GET'])
def get_song_by_id(ID):
    for song in songs:
        if song['ID'] == ID:
            return jsonify({
                'Title': song['Title'],
                'Artist': song['Artist'],
                'Genre': song['Genre'],
                'ID': song['ID'],
                'Release': song['Release']
            })
    abort(404)  # Song not found

@app.route("/songs", methods=['POST'])
def create_song():
    song = {
        'Title': 'New Song',
        'Artist': 'New Artist',
        'Genre': 'Pop',
        'ID': 123128,
        'Release': 2023
    }
    
    songs.append(song)
    return jsonify({'message': 'Song created successfully.', 'song': song}), 201

@app.route("/songs/<int:ID>", methods=['PUT'])
def update_song(ID):
    song = next((s for s in songs if s['ID'] == ID), None)
    if song is None:
        abort(404)  # Song not found

    updated_fields = request.get_json()
    if not updated_fields:
        abort(400)  # Bad request

    song.update(updated_fields)
    return jsonify(song)
    
@app.route("/songs/<int:ID>", methods=['DELETE'])
def delete_song(ID):
    for i, song in enumerate(songs):
        if song['ID'] == ID:
            del songs[i]
            return jsonify({'message': 'Song deleted successfully.'})
    
    abort(404)  # Song not found

# Error handling for common HTTP errors

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request.'}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Song not found.'}), 404

@app.errorhandler(422)
def unprocessable_entity(error):
    return jsonify({'error': 'Unprocessable entity.'}), 422

if __name__ == '__main__':
    app.run(port=5000)