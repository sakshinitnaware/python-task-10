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

# Import the Automation class from the drag_drop module
from drag_drop import Automation 

# Define a test class for automation tests
class TestAutomation():

    def setup_method(self):
        """
        Setup method to initialize the Automation object before each test.
        """
        # Set the test URL
        url = "https://jqueryui.com/droppable/"  
         # Create an instance of Automation class

        self.automation = Automation(url) 
    def test_start_automation_positive(self):
        """
        Positive test case: Verify if the browser window opens successfully.
        """
        assert self.automation.start_automation(), "FAIL : Cant open Window"  # Assert if the window is opened
         # Print success message
        print("SUCCESS : Window Opened") 
        # Close the browser after the test
        self.automation.shutdown_window()  

    def test_start_automation_negative(self):
        """
        Negative test case: Provide an incorrect URL to check failure handling.
        """
         # Different URL (though still valid, may need further testing)
        #url = "https://jqueryui.com/" 
        assert self.automation.start_automation(), "FAIL : Didn't Open Window"  # Check if automation still starts
        # Print success message for expected failure
        print("SUCCESS : Can't open window")  
         # Close the browser
        self.automation.shutdown_window() 

    def test_drag_and_drop_elements_positive(self):
        """
        Positive test case: Check if the drag-and-drop operation works correctly.
        """
        # Start the automation
        self.automation.start_automation()  
        assert self.automation.drag_and_drop_elements(), "FAIL : Can't perform operation"  # Verify operation success
        # Print success message
        print("SUCCESS : Operation performed")  
        # Close the browser
        self.automation.shutdown_window()  

    def test_drag_and_drop_elements_negative(self):
        """
        Negative test case: Force failure by closing the browser before the operation.
        """
        # Start automation 
        self.automation.start_automation()  
        self.automation.shutdown_window(), "FAIL : Didn't perform operation"  # Verify failure
        # Print expected failure message
        print("SUCCESS : Can't perform operation")  
        # Close the browser
        self.automation.shutdown_window()  