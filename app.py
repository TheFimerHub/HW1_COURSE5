from flask import Flask, render_template, request, jsonify
from functions import *

app = Flask(__name__)


@app.route('/movie/<title>')
def search_movie_title_page(title):
    movie = search_fresh_film(title)
    return jsonify(movie)


@app.route('/movie/<int:release_start>/to/<int:release_end>')
def search_movie_range_years(release_start, release_end):
    movie = search_range_release(release_start, release_end)
    return jsonify(movie)


@app.route('/movie/children')
def search_children_movie():
    movie = profile_rating(['G'])
    return jsonify(movie)


@app.route('/movie/family')
def search_family_movie():
    movie = profile_rating(["G", "PG", "PG-13"])
    return jsonify(movie)


@app.route('/movie/adult')
def search_adult_movie():
    return jsonify(profile_rating(['R', 'NC-17']))


@app.route('/genre/<genre>')
def search_movie_genre(genre):
    movie = search_genere(genre)
    return jsonify(movie)


app.run()
