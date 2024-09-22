from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Время ожидания между запросами

    @task
    def login_and_visit_site(self):
        # Аутентификация при старте пользователя
        username = "HR"
        password = "test"
        authenticated_url = f"https://{username}:{password}@qa.digift.ru/"
        self.client.get(authenticated_url)
