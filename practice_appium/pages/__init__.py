# month = 'janyuary'
# year = '2024'
# print(f"//android.widget.TextView[{month} {year}]")
from appium.webdriver.common.appiumby import AppiumBy
class Temp:
    date = ['Febraury', '2024', '18']
    desired_date = f"//android.widget.TextView[@text='{date[0]} {date[1]}']/..//android.widget.TextView[@text='{date[2]}']"


a = Temp()
print(a.desired_date)