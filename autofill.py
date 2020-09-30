from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    StaleElementReferenceException, ElementClickInterceptedException
from selenium import webdriver
import time
from info import info

def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))
        print('Checked out in ', (endTime - startTime) / 1000, 's')
        return result

    return wrapper

@timeme
def order():
    #Go to cart
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="cart"]/div[2]').click()
            break
        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass

    #Checkout as guest
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="btnCheckoutAsGuest"]').click()
            break
        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass

    #First Name
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="billingName1"]').send_keys(info['first'])
            break
        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass

    #Last name
    driver.find_element_by_xpath('//*[@id="billingName2"]').send_keys(info['last'])

    #Address
    driver.find_element_by_xpath('//*[@id="billingAddress1"]').send_keys(info['address'])

    #City
    driver.find_element_by_xpath('//*[@id="billingCity"]').send_keys(info['city'])

    #Zip
    driver.find_element_by_xpath('//*[@id="billingPostalCode"]').send_keys(info['zip'])

    #Phone
    driver.find_element_by_xpath('//*[@id="billingPhoneNumber"]').send_keys(info['phone'])

    #Email
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(info['email'])
    driver.find_element_by_xpath('//*[@id="verEmail"]').send_keys(info['email'])

    #Card
    driver.find_element_by_xpath('//*[@id="ccNum"]').send_keys(info['card'])

    #ExpMonth
    driver.find_element_by_xpath('//*[@id="expirationDateMonth"]/option[{}]'.format(info['expmonth'])).click()

    #ExpYear
    driver.find_element_by_xpath('//*[@id="expirationDateYear"]/option[{}]'.format(info['expyear'])).click()

    #CVV
    driver.find_element_by_xpath('//*[@id="cardSecurityCode"]').send_keys(info['cvv'])


if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')
    link = input("What is the product url?\n")
    driver.get(link)
    notify = True
    while True:
        if notify:
            try:
                driver.find_element_by_xpath('//*[@id="overview_sld1"]/div[1]/div[1]/div/div/div/div[5]/div/div/div/div[2]/a').click()
                break
            except NoSuchElementException:
                pass
            except StaleElementReferenceException:
                pass
            except ElementNotInteractableException:
                pass
            except ElementClickInterceptedException:
                pass

            try:
                driver.find_element_by_xpath('//*[@id="cart"]/div[2]')
                break
            except NoSuchElementException:
                pass
            except StaleElementReferenceException:
                pass
            except ElementNotInteractableException:
                pass
    order()