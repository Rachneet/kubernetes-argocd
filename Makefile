start:
	@bash deploy.sh

install:
	@pip install -r requirements.txt

test:
	@pytest tests