from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    MAIN_URL = 'https://sure-qa-challenge.vercel.app/'
    GET_A_QUOTE_BTN = (By.CSS_SELECTOR, '.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-fullWidth')
    REQUIRED_MESSAGE = (By.CSS_SELECTOR, '.MuiFormHelperText-root.Mui-error')
    ZIP_CODE_FIELD = (By.CSS_SELECTOR, '.MuiInputBase-input.MuiInput-input')
    BRICKS_CHECKBOX = (By.CSS_SELECTOR, 'label[data-testid="bricks"]')
    NEXT_BTN = (By.CSS_SELECTOR, '.MuiButton-label')
    YES_OPTION = (By.XPATH, '//span[contains(text(), "Yes")]')
    INCLUDE_FLOOD_PROTECTION_LABEL = (By.CSS_SELECTOR, '.MuiFormControlLabel-root span.MuiTypography-root.MuiFormControlLabel-label.MuiTypography-body1')
    FLOOD_PROTECTION_CHECKBOX = (By.CSS_SELECTOR, 'span.MuiIconButton-label')
    STANDARD_OPTION = (By.XPATH, '//h3[contains(text(), "Standard")]')
    COMPLETE_OPTION = (By.XPATH, '//h3[contains(text(), "Complete")]')
    PLAN_OPTIONS_BTN = (By.CSS_SELECTOR, '.MuiButton-label')

    def open_main_page(self):
        self.open_url(self.MAIN_URL)

    def click_get_a_quote_button(self):
        self.wait_for_element_to_be_clickable_and_click(*self.GET_A_QUOTE_BTN)

    def verify_error_message(self, message):
        self.verify_text(message, *self.REQUIRED_MESSAGE)

    def enter_zip_code(self, zip_code):
        self.input_text(zip_code, *self.ZIP_CODE_FIELD)

    def select_bricks(self):
        self.wait_for_element_to_be_clickable_and_click(*self.BRICKS_CHECKBOX)

    def click_next_button(self):
        self.wait_for_element_to_be_clickable_and_click(*self.NEXT_BTN)

    def verify_url_query(self, url_query):
        self.verify_partial_url(url_query)

    def select_yes_option(self):
        self.wait_for_element_to_be_clickable_and_click(*self.YES_OPTION)

    def verify_included_flood_protection_label(self):
        label_text = 'Include Flood Protection'
        self.verify_partial_text(label_text, *self.INCLUDE_FLOOD_PROTECTION_LABEL)

    def verify_checkbox_is_unmarked(self):
        assert not self.is_element_checked(*self.FLOOD_PROTECTION_CHECKBOX), f'Checkbox is marked'

    def verify_plan_options(self):
        first_option = 'Standard'
        self.verify_text(first_option, *self.STANDARD_OPTION)
        second_option = 'Complete'
        self.verify_text(second_option, *self.COMPLETE_OPTION)

    def verify_options_clickable(self):
        plan_btns = self.find_elements(*self.PLAN_OPTIONS_BTN)
        for btn in plan_btns:
            assert btn.is_enabled(), f'Button {btn} is not clickable'
