# My Django Project

A Python-based blog, which utilizes Django capabilities. A fun and interactive blog that allows various basic blog site features:

- Listing posts
- Checking recent posts
- Posting comments
- Various post filters
- Saving posts for later read by session
- And more features being added over time.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. **Optional - Set up a virtual environment**
   2.1 **Create venv**
   python -m venv django_site
   2.2 **Activate venv**
   # On Linux/MacOS use source django_site/bin/activate
   # On Windows use `django_site\Scripts\activate`

3.**Install Dependencies**

    'pip install -r requirements.txt

4.**Optional - Migrate DB to set up a new DB**

    # python manage.py makemigrations
    # python manage.py migrate

5. **Run Development Server**
   python manage.py runserver

## Usage

- Access the blog at http://127.0.0.1:8000/.

- Interact with the blog by listing posts, checking recent posts, posting comments, using various post filters, and saving posts for later read.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Third-Party Licenses

This project uses the following dependencies, which have their own licenses:

- **Django**: Licensed under the BSD License. See the [Django license](https://docs.djangoproject.com/en/stable/misc/design-philosophies/#license).
- **Python**: Licensed under the Python Software Foundation License. See the [Python license](https://docs.python.org/3/license.html).
- **Pillow**: Licensed under the Historical Permission Notice and Disclaimer (HPND) License. See the [Pillow license](https://pillow.readthedocs.io/en/stable/about.html#license).

## Acknowledgments

This project uses SQLite, which is a public domain software package.
