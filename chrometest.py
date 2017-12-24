from selenium import webdriver
browser = webdriver.Chrome(executable_path="/Users/raffles/Downloads/chromedriver")
url = "https://www.duckduckgo.com"
browser.get(url)
browser.maximize_window()

search_bar = browser.find_element_by_xpath("//input[@id='search_form_input_homepage']")

search_bar.send_keys("python")


search_button = browser.find_element_by_xpath("//input[@id='search_button_homepage']")

search_button.click()

search_results = browser.find_elements_by_xpath("//div[@id='links']/div/div/h2/a[@class='result__a']")
print(len(search_results))
for result in search_results:
    print(result.text)

urls=[]
for result in search_results:
    urls.append(result.get_attribute("href"))

for url in urls:
    print(url)

browser.quit()


