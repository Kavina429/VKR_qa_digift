from locust import HttpUser, task, between
from playwright.sync_api import sync_playwright, Page, BrowserContext

# Определение функции get_cookies
def get_cookies():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        authenticated_url = "https://HR:test@qa.digift.ru/"
        page.goto(authenticated_url)

        # Получаем куки
        cookies = context.cookies()
        context.close()
        browser.close()
        return cookies

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Время ожидания между запросами

    def on_start(self):
        # Аутентификация при старте пользователя
        self.authenticated_url = "https://HR:test@qa.digift.ru/"
        self.client.get(self.authenticated_url)

        # Получаем куки с помощью Playwright
        self.cookies = get_cookies()

    @task
    def send_post_request(self):
        # Формируем строку с куки для заголовка Cookie
        cookie_string = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in self.cookies])

        # Устанавливаем заголовок Cookie для клиента Locust
        self.client.headers.update({"Cookie": cookie_string})

        payload = {
            "card_template_id": "7",
            "value": "2000",
            "custom_image_original": "",
            "custom_image": "",
            "user_name": "Name",
            "user_lastname": "",
            "user_email": "pochta@mail.ru",
            "user_mobile": "",
            "width": "1586",
            "sender_text": "",
            "nominal_value": "2000",
            "sender_name": "Name",
            "sender_lastname": "",
            "sender_email": "pochta@mail.ru",
            "sender_mobile": "",
            "receiver_name": "Name2",
            "receiver_lastname": "",
            "receiver_email": "pochta2@mail.ru",
            "receiver_mobile": "",
            "delivery_date": "сегодня",
            "delivery_date": "22.09.2024",
            "delivery_time": "13",
            "to_checkout": "1"
        }

        # Отправляем POST-запрос на главную страницу
        response = self.client.post(self.authenticated_url, json=payload)

        # Проверяем статус ответа
        if response.status_code == 302:
            # Получаем URL перенаправления из заголовка Location
            redirect_url = response.headers.get('Location')
            print(f"Redirect URL: {redirect_url}")

            # Отправляем GET-запрос на URL перенаправления
            response = self.client.get(redirect_url)

            # Проверяем статус ответа
            if response.status_code == 302:
                # Получаем URL второго перенаправления из заголовка Location
                redirect_url = response.headers.get('Location')
                print(f"Second Redirect URL: {redirect_url}")

                # Отправляем GET-запрос на второй URL перенаправления
                response = self.client.get(redirect_url)

                # Проверяем статус ответа
                if response.status_code == 302:
                    # Получаем URL третьего перенаправления из заголовка Location
                    redirect_url = response.headers.get('Location')
                    print(f"Third Redirect URL: {redirect_url}")

                    self.client.get(redirect_url)
            elif response.status_code == 200:
                    print(f"Received 200 status code. Response content: {response.content}")
            else:
                    print(f"Unexpected status code: {response.status_code}")

    # locust -f locustfile.py --host=https://qa.digift.ru/
