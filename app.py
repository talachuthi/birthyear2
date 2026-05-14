from flask import Flask, jsonify, request

app = Flask(__name__)

# ----------------------------
# Sample in-memory database
# ----------------------------
books = [
    {"id": 1, "book_name": "1984", "author": "George Orwell", "publisher": "Secker & Warburg"},
    {"id": 2, "book_name": "To Kill a Mockingbird", "author": "Harper Lee", "publisher": "J.B. Lippincott & Co."}
]

# ----------------------------
# GET all books
# ----------------------------
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# ----------------------------
# GET book by ID
# ----------------------------
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    
    if book:
        return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# ----------------------------
# CREATE a new book
# ----------------------------
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json

    new_book = {
        "id": books[-1]["id"] + 1 if books else 1,
        "book_name": data["book_name"],
        "author": data["author"],
        "publisher": data["publisher"]
    }

    books.append(new_book)
    return jsonify(new_book), 201

# ----------------------------
# UPDATE a book
# ----------------------------
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json

    book = next((b for b in books if b["id"] == book_id), None)

    if not book:
        return jsonify({"message": "Book not found"}), 404

    book["book_name"] = data.get("book_name", book["book_name"])
    book["author"] = data.get("author", book["author"])
    book["publisher"] = data.get("publisher", book["publisher"])

    return jsonify(book)

# ----------------------------
# DELETE a book
# ----------------------------
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]

    return jsonify({"message": "Book deleted successfully"})

# ----------------------------
# RUN SERVER
# ----------------------------
if __name__ == '__main__':
    app.run(debug=True)