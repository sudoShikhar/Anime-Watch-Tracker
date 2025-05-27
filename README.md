# Anime Watch Tracker

A Django web app to track your anime watching progress. Users can register, log in, add anime to their watchlist, update progress, and remove tracked anime.

## Features

- User registration and authentication
- Add, update, and delete anime tracking entries
- Progress bar for watched episodes
- Responsive UI with Bootstrap

## Setup Instructions

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/Anime-Watch-Tracker.git
cd Anime-Watch-Tracker
```

### 2. Create and activate a virtual environment

```sh
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix/macOS:
source venv/bin/activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Apply migrations

```sh
python AnimeWebsite/manage.py migrate
```

### 5. Create a superuser (optional, for admin access)

```sh
python AnimeWebsite/manage.py createsuperuser
```

### 6. Run the development server

```sh
python AnimeWebsite/manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Useful Links

- [Bootstrap Forms Example](https://getbootstrap.com/docs/5.3/examples/sign-in/)
- [Django Authentication Customization](https://stackoverflow.com/a/55369752)
- [Django User Authentication Docs](https://docs.djangoproject.com/en/4.1/topics/auth/default/)

## Notes

- To deactivate the virtual environment, run `deactivate`.
- The database file `db.sqlite3` is ignored by git.
- For deployment, update `ALLOWED_HOSTS` and set `DEBUG = False` in `AnimeWebsite/settings.py`.

---

### Developer

- Built by [Shikhar](https://www.linkedin.com/in/shikhar-sharma-1b9a7b1b2/)
- [Project Showcase](https://sudoShikhar.github.io/)
- [Source Code on GitHub](https://github.com/sudoShikhar/Anime-Watch-Tracker)
