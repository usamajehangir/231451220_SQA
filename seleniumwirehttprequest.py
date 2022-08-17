from seleniumwire import webdriver  # Import from seleniumwire

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Go to the Google home page
driver.get('https://www.python.org')

# Access and print requests via the `requests` attribute
for request in driver.requests:
	if request.response:
		print(
			request.url,
			request.response.status_code,
			request.response.headers['Content-Type'])
