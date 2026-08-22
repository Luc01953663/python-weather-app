from api import get_weather_for_location

location = input("Enter location: ")
state = input("Enter state: ")

def main():
    get_weather_for_location(location, state)
    pass

if __name__ == "__main__":
    main()

