package prac4;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;

public class LoginTest {
	public static void main(String[] args) throws InterruptedException {
		FirefoxOptions options = new FirefoxOptions();
		options.setBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe");
		System.setProperty("webdriver.gecko.driver", "C:\\Users\\User1\\Downloads\\selenium webdriver\\geckodriver.exe");
		WebDriver driver = new FirefoxDriver(options);
		driver.get("https://accounts.google.com/");
		driver.findElement(By.id("identifierId")).sendKeys("example@gmail.com");
		driver.findElement(By.id("identifierNext")).click();
//		driver.findElement(By.name("password")).sendKeys("PASSWORD1234");
//		driver.findElement(By.id("passwordNext")).click();
		String title = driver.getTitle();
		
		if (title.equals("Google Account")) {
			System.out.println("Login Successful");
		} else {
			System.out.println("Login Failed");
		}
		driver.quit();
		
	}
}
