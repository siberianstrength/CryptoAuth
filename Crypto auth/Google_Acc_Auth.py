from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def get_words(filename: str) -> str:
    """
    Recieves file name and yields seed words.

    Parameters
    ----------
    filename : string 
    # file extension is required

    Yields
    ------
    string values

    """
    with open(f'{filename}') as f:
        data = f.readlines()
    for word in data:
        yield word.rstrip()
    
    
def click_button(driver, element_id: str) -> None or Exception:
    """
    Recieves driver and element id from html page. 
    Clicks button if found, else returns error.

    Parameters
    ----------
    driver : webdriver
    element_id : str

    Returns
    -------
    None or Exception
    
    """
    try:
        checkbox = driver.find_element(By.XPATH, f'//*[@data-testid="{element_id}"]')
        checkbox.click()
        
    except Exception as e:
        return e
    
def run_chrome(port: int, filename: str) -> None:
    """
    Completes authorization process in MetaMask using seed words.

    Parameters
    ----------
    port : int
    filename: str

    Returns
    -------
    None

    """
    options = Options()
    options.add_experimental_option(
       "debuggerAddress", f"localhost:{port}")
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=ChromeService(
       ChromeDriverManager(chrome_type="chromium").install()), options=options)
    driver.execute_script("window.focus();")
    
    driver.get('chrome-extension://cfkgdnlcieooajdnoehjhgbmpbiacopjflbjpnkm/home.html')
    time.sleep(1)
    try:
        EXTENSION_ID = 'cfkgdnlcieooajdnoehjhgbmpbiacopjflbjpnkm'
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))
        
        driver.switch_to.window(driver.window_handles[0])
        
    except:
        pass
    
    time.sleep(1)
    try:
        click_button(driver, 'onboarding-terms-checkbox')

    except:
        print('Error has occured while locating or pressing checkbox')
    
    time.sleep(1)
    try:
        click_button(driver, 'onboarding-import-wallet')
        
    except:
        print('Error has occured while locating or importing wallet')
        
    time.sleep(1)   
    try:
        click_button(driver, 'metametrics-i-agree')
        
    except:
        print('Error has occured while locating or pressing agreement button')
    
    time.sleep(1)
    i = 0
    for seed_word in get_words(filename):
        try:
            field = driver.find_element(By.XPATH, f'//*[@data-testid="import-srp__srp-word-{i}"]')
            field.click()
            field.send_keys(f'{seed_word}')
            i += 1
            
        except:
            print('Error has occured while inserting or locating seed words')
            
    time.sleep(1)
    try:
        click_button(driver, 'import-srp-confirm')
        
    except:
        print('Error has occured while locating/clicking confirmation button')   
        
    # create new password window    
    try:
        password = driver.find_element(By.XPATH, f'//*[@data-testid="create-password-new"]')
        password.click()
        password.send_keys(f'password123')
        
        confirmation = driver.find_element(By.XPATH, f'//*[@data-testid="create-password-confirm"]')
        confirmation.click()
        confirmation.send_keys('password123')
        
        click_button(driver, 'create-password-terms')
        time.sleep(.5)
        click_button(driver, 'create-password-import')
        time.sleep(.5)
        click_button(driver, 'onboarding-complete-done')
        click_button(driver, 'pin-extension-next')
        time.sleep(.5)
        click_button(driver, 'pin-extension-done')
        
    except:
        print('Error has occured while creating password')