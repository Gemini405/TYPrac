package seleniumDemo;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;

public class SeleniumScript {

	public static void main(String[] args) {
		FirefoxOptions options = new FirefoxOptions();
	    options.setBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe");
		System.setProperty("webdriver.gecko.driver", "C:\\Users\\User1\\Downloads\\selenium webdriver\\geckodriver.exe");
		WebDriver driver = new FirefoxDriver(options);
		driver.get("https://facebook.com/");
		System.out.println(driver.getTitle());
		driver.quit();
	}
}
