# Import Selenium modules for browser automation
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Svc
from webdriver_manager.chrome import ChromeDriverManager as CDM
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException 
chrome_options = Options()

# Create Chrome options for browser configuration
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run browser in headless mode (no UI)
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration for better performance in headless mode
chrome_options.add_argument('--window-size=1920x1080')  # Set browser window size for proper element detection
# chrome_options.add_argument('--no-sandbox')  # Uncomment if running in an environment where sandboxing causes issues
chrome_options.add_argument('--disable-dev-shm-usage')  # Fix memory-related issues

# Define the target URL for automation
url = "https://jqueryui.com/droppable/"

# Define a class to store element locators
class Locators:
     # XPath for the draggable element
    drag_object = '//*[@id = "draggable"]' 
    # XPath for the droppable container
    drop_container = '//*[@id = "droppable"]'  

# Define the main automation class
class Automation:
    def __init__(self, url):
        """
        Initialize the WebDriver, ActionChains, and WebDriverWait.
        :param url: URL of the webpage to be automated.
        """
        self.url = url
        # Launch Chrome browser
        self.driver = webdriver.Chrome(service=Svc(CDM().install()), options=chrome_options) 
         
        # Initialize ActionChains for interactions like drag-and-drop
        self.action = ActionChains(self.driver) 
        # Set an explicit wait time of 10 seconds 
        self.wait = WebDriverWait(self.driver, 10)  

    def start_automation(self):
        """
        Opens the browser, navigates to the given URL, maximizes the window,
        and switches to the correct iframe (since the droppable element is inside an iframe).
        """
        try:
            # Open the target URL
            self.driver.get(self.url)  
            # Maximize the browser window
            self.driver.maximize_window()  
            print("Window successfully opened")
            # Switch to iframe containing elements
            self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, "iframe"))
            # Return True if successful
            return True  
        except Exception as E:
            print(f"Exception occurred while opening the window: {E}")
            # Return False if an error occurs
            return False  

     # Closes the browser window and ends the session.
    def shutdown_window(self):
        try:
            # Close the browser
            self.driver.quit()  
        except Exception as E:
             # Handle exceptions if browser fails to close
            print(f"Window couldn't shut down: {E}") 

    def drag_and_drop_elements(self):
        """
        Performs the drag-and-drop operation between the draggable object and the drop container.
        Returns True if successful, otherwise returns False.
        """
        try:
            # Wait for the draggable element to be present and get its reference
            drag_locator = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.drag_object)))
            print("Drag object found")

            # Wait for the drop container to be present and get its reference
            drop_locator = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.drop_container)))
            print("Drop object found")

            # Perform drag-and-drop operation
            self.action.drag_and_drop(drag_locator, drop_locator).perform()
            print("Successful Drag and Drop")
            return True  # Return True if drag-and-drop is successful
        except (NoSuchElementException, ElementNotInteractableException, TimeoutException) as E:
            # Handle exceptions if elements are not found or cannot be interacted with
            print(f"Exception: {E}")  
            return False  # Return False if drag-and-drop fails

# Uncomment the following lines to run the script independentlyv
# if __name__ == "__main__" :
#     automation = Automation(url)
#     automation.start_automation()
#     automation.drag_and_drop_elements()
#     automation.shutdown_window()

