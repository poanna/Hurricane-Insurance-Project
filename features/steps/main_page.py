from behave import given, when, then


@given('Open the main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('Click on Get a Quote button')
def click_get_a_quote_button(context):
    context.app.main_page.click_get_a_quote_button()


@when('Enter {zip_code} in zip code field')
def enter_zip_code(context, zip_code):
    context.app.main_page.enter_zip_code(zip_code)


@when('Select Bricks on Building Materials')
def select_bricks(context):
    context.app.main_page.select_bricks()


@when('Select yes on Water Proximity question')
def select_option(context):
    context.app.main_page.select_yes_option()


@when('Click on Next button')
def click_next_button(context):
    context.app.main_page.click_next_button()


@then('User can see {message} message')
def verify_required_message(context, message):
    context.app.main_page.verify_error_message(message)


@then('Verify {url_query} page opened')
def verify_url_query(context, url_query):
    context.app.main_page.verify_url_query(url_query)


@then('Verify Include Flood Protection label')
def verify_label(context):
    context.app.main_page.verify_included_flood_protection_label()


@then('Verify checkbox is unmarked')
def verify_checkbox_is_unmarked(context):
    context.app.main_page.verify_checkbox_is_unmarked()


@then('Verify two plan options')
def verify_options(context):
    context.app.main_page.verify_plan_options()


@then('Verify plan options are clickable')
def verify_options(context):
    context.app.main_page.verify_options_clickable()
