from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Dummy movie recommendation function for testing
def get_recommendations(title, cosine_sim):
    return ["Movie 1", "Movie 2", "Movie 3"]

@app.route('/')
def home():
    return '''
    <html>
    <body>
        <form action="/recommend" method="post">
            Movie name: <input type="text" name="movie_name">
            <input type="submit">
        </form>
    </body>
    </html>
    '''

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_name = request.form['movie_name']
    recommendations = get_recommendations(movie_name, None)
    return f'''
    <html>
    <body>
        <h1>Recommendations for {movie_name}</h1>
        <ul>
            {''.join(f'<li>{movie}</li>' for movie in recommendations)}
        </ul>
        <a href="/">Back</a>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
