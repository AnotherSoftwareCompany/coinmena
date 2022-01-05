build:
	docker-compose build
run:
	docker-compose up
migrate:
	docker-compose exec -it app python manage.py migrate
