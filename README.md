# Book Catalog API Project

This project is a Django-based Web API for a Book Store. It includes models for books, authors, and genres, and provides an admin interface for managing these entities.

## Features

- Manage books, authors, and genres
- Upload images for books and authors
- Admin interface for managing the bookstore

## Requirements

- Python
- pip

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the admin interface:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Access the application at `http://127.0.0.1:8000/` and the admin interface at `http://127.0.0.1:8000/admin/`.

## Usage

- Use the admin interface to add and manage books, authors, and genres.
- Upload images for books and authors through the admin interface.

## Models

### Book

- `title`: CharField
- `author`: ManyToManyField (to `Author`)
- `year`: IntegerField
- `genre`: ForeignKey (to `Genre`, on_delete=RESTRICT)
- `publisher`: CharField
- `isbn`: CharField
- `image`: ImageField
- `description`: TextField

### Author

- `name`: CharField
- `bio`: TextField
- `image`: ImageField (optional)

### Genre

- `name`: CharField

## License

This project is licensed under the MIT License.