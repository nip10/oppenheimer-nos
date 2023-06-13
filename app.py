import requests
import json
import schedule
import time
from playsound import playsound


def fetch_and_print_data():
    print("\n" + "*" * 50)
    print("Fetching data from the endpoint...")
    print("*" * 50 + "\n")
    url = "https://www.cinemas.nos.pt/graphql/execute.json/cinemas/getTopMovies"
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        items = data["data"]["movieList"]["items"]

        pre_sale_movies = [
            item for item in items if item["moviestate"] == "PreSale"]
        print("Movies in PreSale state:")
        for movie in pre_sale_movies:
            print(movie["title"])

        oppenheimer_movies = [
            item for item in items if "oppenheimer" in item["originaltitle"].lower()]
        if oppenheimer_movies:
            print("\n" + "*" * 50)
            print("ATTENTION: Movies with 'Oppenheimer' in the original title:")
            for movie in oppenheimer_movies:
                print(movie["title"])
            print("*" * 50 + "\n")

            # Play an alert sound
            # You need to have a file called 'alert.mp3' in the same directory
            playsound('alert.mp3')
        else:
            print("\nNo movie with 'Oppenheimer' in the original title found.")
    else:
        print("Failed to fetch data from the endpoint.")

    print("\n" + "*" * 50)
    print("Script finished running.")
    print("*" * 50 + "\n")


if __name__ == "__main__":
   # Display a message when the script starts running
    print("Script started. Fetching and printing data every hour.")

    # Run the script immediately
    fetch_and_print_data()

    # Schedule the task at 1-hour intervals
    schedule.every(1).hours.do(fetch_and_print_data)

    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(1)
