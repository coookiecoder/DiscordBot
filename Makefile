run:
	mkdir -p /database_data
	docker compose up --build --detach

stop:
	docker compose down

clean: stop
	docker system prune -af
	rm -rf /database_data
	mkdir -p /database_data

open_bot:
	docker exec -it bot /bin/sh

open_database:
	docker exec -it database /bin/sh
