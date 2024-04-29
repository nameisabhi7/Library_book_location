from flask import Flask, render_template, request
import csv

def load_book_data(file_path):
    book_data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            book_data.append(row)
    return book_data

def find_book_location(book_data, book_title):
    for book in book_data:
        if book['Title'].lower() == book_title.lower():
            return book
    return "Book not found"

app = Flask(__name__, template_folder='.')

# Load book data
book_dataset = 'book_data.csv'
book_data = load_book_data(book_dataset)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        book_title = request.form['book_title']
        book_info = find_book_location(book_data, book_title)
    else:
        book_info=None

    return render_template('index.html', book_info=book_info)
    

if __name__ == '__main__':
    app.run(debug=True)