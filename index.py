import mechanicalsoup

# GET LOGIN SESSIONS
browser = mechanicalsoup.StatefulBrowser()
browser.open("URL_FORM_LOGIN")
browser.select_form('form[action="URL_FORM_ACTION"]')
browser["username"] = "YOUR_USERNAME"
browser["password"] = "YOUR_PASSWORD"
browser.submit_selected()

# GET URL YOU NEED
browser.open("URL_THAT_YOU_WANT_ACCESS")
page = browser.get_current_page()
