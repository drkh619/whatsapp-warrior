from selenium import webdriver

# start a Chrome driver instance
driver = webdriver.Chrome()

# navigate to the WhatsApp Web page
driver.get('https://web.whatsapp.com/')

# wait for the user to scan the QR code and log in
input("Press Enter after scanning QR code and logging in")

# find the desired contact's chat header using the CSS selector
contact = driver.find_element_by_css_selector('span[title="CONTACT_NAME"]')

# click on the contact's chat header to open the chat
contact.click()

# check if the contact is online by looking for the "online" label
while True:
    try:
        online_label = driver.find_element_by_css_selector('._3qeKj span')
        if online_label.text == 'online':
            print('Contact is online')
            break
    except:
        print('Contact is offline')

# close the driver instance
driver.quit()
