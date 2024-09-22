from config import *
from data import *
from locator import *


@pytest.fixture
def login(page: Page):
    def login_function(username, password):
        authenticated_url = f"https://{username}:{password}@qa.digift.ru/"
        page.goto(authenticated_url)
    return login_function

@pytest.fixture
def end_to_end_1(page: Page):
    def end_to_end_1_function():
        page.click(locator_kart_file)
        file_path = './files/gerbera.jpg'     # путь к файлу
        page.set_input_files('input[type="file"]', file_path)
        page.click(locator_button_accept)
        page.wait_for_timeout(1000)
        page.locator(locator_input_text).fill(data_text)
        page.click(locator_nominal_5000)
        page.wait_for_timeout(1000)
        page.screenshot(path='screen/design.png')
        page.wait_for_timeout(2000)
        page.locator(locator_field_name_from).fill(data_name_from)
        page.locator(locator_field_lastname_from).fill(data_lastname_from)
        page.locator(locator_field_mail_from).fill(data_mail_from)
        page.locator(locator_field_phone_from).fill(data_phone_from)
        page.wait_for_timeout(1000)
        page.locator(locator_field_name_to).fill(data_name_to)
        page.locator(locator_field_lastname_to).fill(data_lastname_to)
        page.locator(locator_field_mail_to).fill(data_mail_to)
        page.locator(locator_field_phone_to).fill(data_phone_to)
        page.wait_for_timeout(1000)
        page.click(locator_field_calender)
        tomorrow_date = get_segodnya()
        tomorrow_date_str = format_date(tomorrow_date)  # Преобразование даты в строку
        page.keyboard.type(tomorrow_date_str)
        page.wait_for_timeout(2000)
        page.keyboard.down('ControlLeft')
        page.keyboard.press('Enter')
        page.keyboard.up('ControlLeft')
        page.keyboard.press('Tab')
        page.wait_for_timeout(2000)
        locator_validity_period_locator = page.locator(locator_validity_period)
        page.wait_for_timeout(1000)
        # Получаем дату через 3 месяца
        date_in_three_months = get_date_in_three_months(tomorrow_date)
        date_in_three_months_str = format_date(date_in_three_months)  # Преобразуем в строку
        # Формируем строку с датами для ассерта
        expected_text = f"{tomorrow_date_str} – {date_in_three_months_str}"
        expect(locator_validity_period_locator).to_have_text(expected_text)
        page.wait_for_timeout(1000)
        page.click(locator_field_time)
        page.wait_for_timeout(1000)
        page.select_option('select[name="delivery_time"]', label='15:00 — 16:00 (мск)')
        page.keyboard.press('Enter')
        page.wait_for_timeout(1000)
        select_text_locator = page.locator('div.jq-selectbox__select-text')
        expect(select_text_locator).to_have_text('15:00 — 16:00 (мск)')
        page.wait_for_timeout(1000)
        page.screenshot(path='screen/form.png')
        page.wait_for_timeout(1000)
        page.click(locator_go_to_payment)
        page.wait_for_timeout(1000)
        assert page.inner_text('h1') == data_assert_1
    return end_to_end_1_function

@pytest.fixture
def end_to_end_2(page: Page):
    def end_to_end_2_function():
        page.click(locator_kart_feather)
        page.wait_for_timeout(1000)
        page.locator(locator_input_text).fill(data_text)
        page.locator(locator_nominal_input).fill(data_nominal)
        page.wait_for_timeout(1000)
        page.screenshot(path='screen/design2.png')
        page.wait_for_timeout(2000)
        page.locator(locator_field_name_from).fill(data_name_from)
        page.locator(locator_field_lastname_from).fill(data_lastname_from)
        page.locator(locator_field_mail_from).fill(data_mail_from)
        page.locator(locator_field_phone_from).fill(data_phone_from)
        page.wait_for_timeout(1000)
        page.locator(locator_field_name_to).fill(data_name_to)
        page.locator(locator_field_lastname_to).fill(data_lastname_to)
        page.locator(locator_field_mail_to).fill(data_mail_to)
        page.locator(locator_field_phone_to).fill(data_phone_to)
        page.wait_for_timeout(1000)
        page.click(locator_button_calender)
        page.keyboard.down('ControlLeft')
        for _ in range(6):
            page.keyboard.press('ArrowRight')
        page.keyboard.press('Enter')
        page.keyboard.up('ControlLeft')
        page.wait_for_timeout(2000)
        page.click(locator_field_time)
        page.wait_for_timeout(1000)
        page.select_option('select[name="delivery_time"]', label='17:00 — 18:00 (мск)')
        page.keyboard.press('Enter')
        page.wait_for_timeout(1000)
        select_text_locator = page.locator('div.jq-selectbox__select-text')
        expect(select_text_locator).to_have_text('17:00 — 18:00 (мск)')
        page.wait_for_timeout(1000)
        page.screenshot(path='screen/form2.png')
        page.wait_for_timeout(1000)
        page.click(locator_go_to_payment)
        page.wait_for_timeout(1000)
        order_payed_text = page.inner_text('div.order-payed__text')
        expected_text = data_assert_2
        assert order_payed_text == expected_text, f"Expected text: '{expected_text}', but got: '{order_payed_text}'"
    return end_to_end_2_function


@pytest.fixture
def end_to_end_3(page: Page):
    def end_to_end_3_function():
        page.click(locator_kart_file)
        file_path = './files/gerbera.jpg'
        page.set_input_files('input[type="file"]', file_path)
        page.click(locator_button_accept)
        page.wait_for_timeout(1000)
        page.click(locator_kart_present)
        page.wait_for_timeout(1000)
        page.locator(locator_input_text).fill(data_text)
        page.click(locator_nominal_10000)
        page.wait_for_timeout(1000)
        page.screenshot(path='screen/design3.png')
        page.wait_for_timeout(2000)
        page.locator(locator_field_name_from).fill(data_name_from)
        page.locator(locator_field_lastname_from).fill(data_lastname_from)
        page.locator(locator_field_mail_from).fill(data_mail_from)
        page.locator(locator_field_phone_from).fill(data_phone_from)
        page.wait_for_timeout(1000)
        page.click(locator_checkbox_for_me)
        page.wait_for_timeout(1000)
        page.screenshot(path='screen/for_me.png')
        page.wait_for_timeout(1000)
        page.click(locator_field_calender)
        sevenday_date = get_sevenday()
        sevenday_date_str = format_date(sevenday_date)
        page.keyboard.type(sevenday_date_str)
        page.wait_for_timeout(2000)
        page.keyboard.down('ControlLeft')
        page.keyboard.press('Enter')
        page.keyboard.up('ControlLeft')
        page.keyboard.press('Tab')
        page.wait_for_timeout(2000)
        page.click(locator_field_time)
        page.wait_for_timeout(1000)
        page.select_option('select[name="delivery_time"]', label='15:00 — 16:00 (мск)')
        page.keyboard.press('Enter')
        page.wait_for_timeout(1000)
        select_text_locator = page.locator('div.jq-selectbox__select-text')
        expect(select_text_locator).to_have_text('15:00 — 16:00 (мск)')
        page.wait_for_timeout(1000)
        page.screenshot(path='screen/form3.png')
        page.wait_for_timeout(1000)
        page.click(locator_go_to_payment)
        page.wait_for_timeout(1000)
        assert page.inner_text('h1') == data_assert_1
    return end_to_end_3_function
