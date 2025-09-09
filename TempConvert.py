#TempConvert.py
#Name: Tessa Horn
#Date: 09/08/2025
#Assignment: Temp Convert Lab 3


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
 tempF = float(input("Enter the temperature in fahrenheit: "))
 tempC = (tempF - 32) * 5 / 9
 tempC2 = tempC
 tempC3 = round(tempC2, 1)

 print (str(tempF) + " degrees fahrenheit is " + str(tempC3) + " degrees celcius")

  
if __name__ == '__main__':
  main()
