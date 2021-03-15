from flask import jsonify, request, abort

from audio import db
from audio.controllers.apiv1 import api_v1
from audio.models.binary import Song, Podcast, Audiobook

ACCEPTED_TYPE = ['Song', "Podcast", "Audiobook"]


@api_v1.route('/get/<file_type>/<int:file_id>', methods=["GET"])
def gets(file_type, file_id):
    if file_type not in ACCEPTED_TYPE:
        abort(400)

    if file_type == 'Song':
        song = Song.query.filter_by(id=file_id).first()
        if song:
            return jsonify(song.as_dict()), 200

    if file_type == 'Podcast':
        podcast = Podcast.query.filter_by(id=file_id).first()
        if podcast:
            return jsonify(podcast.as_dict()), 200

    if file_type == 'Audiobook':
        audiobook = Audiobook.query.filter_by(id=file_id).first()
        if audiobook:
            return jsonify(audiobook.as_dict()), 200

    abort(400)


@api_v1.route('/delete/<file_type>/<int:file_id>', methods=["DELETE"])
def deletes(file_type, file_id):
    if file_type not in ACCEPTED_TYPE:
        abort(400)

    if file_type == 'Song':
        song = Song.query.filter_by(id=file_id).first()
        if song:
            db.session.delete(song)
            db.session.commit()
            return jsonify({'result': True}), 200

    if file_type == 'Podcast':
        podcast = Podcast.query.filter_by(id=file_id).first()
        if podcast:
            db.session.delete(podcast)
            db.session.commit()
            return jsonify({'result': True}), 200

    if file_type == 'Audiobook':
        audio_book = Audiobook.query.filter_by(id=file_id).first()
        if audio_book:
            db.session.delete(audio_book)
            db.session.commit()
            return jsonify({'result': True}), 200

    abort(400)


@api_v1.route('/update/<file_type>/<int:file_id>', methods=["PUT"])
def updates(file_type, file_id):
    if file_type not in ACCEPTED_TYPE:
        abort(400)

    audio_file_metadata = request.json.get('audioFileMetadata')

    if file_type == 'Song':
        duration = audio_file_metadata.get('duration')
        name = audio_file_metadata.get('name')

        song = Song.query.filter_by(id=file_id).first()

        if song:
            if duration:
                song.duration = duration

            if name:
                song.name = name

            db.session.add(song)
            db.session.commit()

            return jsonify({'result': song.as_dict()}), 200

    if file_type == 'Podcast':
        duration = audio_file_metadata.get('duration')
        name = audio_file_metadata.get('name')
        host = audio_file_metadata.get('host')
        participants = audio_file_metadata.get('participants')

        if participants:
            if len(participants) > 10 or [x for x in participants if len(x) > 100]:
                abort(400)

        podcast = Podcast.query.filter_by(id=file_id).first()

        if podcast:
            if duration:
                podcast.duration = duration

            if name:
                podcast.name = name

            if host:
                podcast.name = host

            if participants:
                podcast.participants = participants

            db.session.add(podcast)
            db.session.commit()

            return jsonify({'result': podcast.as_dict()}), 200

    if file_type == 'Audiobook':
        duration = audio_file_metadata.get('duration')
        title = audio_file_metadata.get('title')
        author = audio_file_metadata.get('author')
        narration = audio_file_metadata.get('narration')

        audiobook = Audiobook.query.filter_by(id=file_id).first()

        if audiobook:
            if duration:
                audiobook.duration = duration

            if title:
                audiobook.title = title

            if author:
                audiobook.author = author

            if narration:
                audiobook.narration = narration

            db.session.add(audiobook)
            db.session.commit()

            return jsonify({'result': audiobook.as_dict()}), 200


@api_v1.route('/create', methods=["POST"])
def creates():
    audio_file_type = request.json['audioFileType']

    if audio_file_type not in ACCEPTED_TYPE:
        abort(400)

    audio_file_metadata = request.json['audioFileMetadata']

    if audio_file_type == 'Song':
        name, duration = song_verification(audio_file_metadata)
        song = Song(name=name, duration=duration)
        db.session.add(song)
        db.session.commit()

        return jsonify({'success': song.as_dict()}), 200

    if audio_file_type == 'Podcast':
        name, duration, host, participants = podcast_verification(audio_file_metadata)

        podcast = Podcast(name=name, duration=duration, host=host)
        if participants:
            podcast.participants = participants

        db.session.add(podcast)
        db.session.commit()

        return jsonify({'success': podcast.as_dict()}), 200

    if audio_file_type == 'Audiobook':
        title, author, narrator, duration = audio_book_verification(audio_file_metadata)

        audio_book = Audiobook(title=title, author=author, narrator=narrator, duration=duration)
        db.session.add(audio_book)
        db.session.commit()

        return jsonify({'success': audio_book.as_dict()}), 200


def song_verification(audio_file_metadata):
    duration = audio_file_metadata.get('duration')
    name = audio_file_metadata.get('name')

    if not all([name, duration]):
        abort(400)

    confirm_name = Song.query.filter_by(name=name).first()
    if confirm_name:
        abort(400)

    return name, duration


def audio_book_verification(audio_file_metadata):
    duration = audio_file_metadata.get('duration')
    title = audio_file_metadata.get('title')
    author = audio_file_metadata.get('author')
    narrator = audio_file_metadata.get('narrator')

    if not all([title, author, narrator, duration]):
        abort(400)

    confirm_audio_book = Audiobook.query.filter_by(title=title, author=author, narrator=narrator).first()
    if confirm_audio_book:
        abort(400)

    return title, author, narrator, duration


def podcast_verification(audio_file_metadata):
    name = audio_file_metadata.get('name')
    duration = audio_file_metadata.get('duration')
    host = audio_file_metadata.get('host')
    participants = audio_file_metadata.get('participants')

    if not all([name, duration, host]):
        abort(400)

    if participants:
        if len(participants) > 10 or [x for x in participants if len(x) > 100]:
            abort(400)

    confirm_podcast = Podcast.query.filter_by(name=name, duration=duration, host=host).first()
    if confirm_podcast:
        abort(400)

    return name, duration, host, participants
