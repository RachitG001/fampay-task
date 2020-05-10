# Fampay backend hiring task
Hi, i have created an api to fetch latest videos from youtube in reverse chronological order of their publishing date-time for tag cricket. The result will be a paginated response with page size limit of 10 queries each.

### Techstack used:
- Django for backend
- Postgres for database

### Features implemented
- Get api to fetch videos
- Background task to call youtube apis after every 100 sec
- Implemented queue to use multiple api keys if one fails (Implemented roundrobin method)
- Created a dashboard with sorting option based on published date and title.

### Instructions to run the server:
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver
- python manage.py process_tasks
  (Note: Comment background tasks command before making migrations.)