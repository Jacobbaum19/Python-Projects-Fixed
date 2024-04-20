from bs4 import BeautifulSoup
import requests


# Find the top 100 movies, put it into a list and flip it to display it from 100- 1.


movie_page = requests.get(url="https://www.imdb.com/list/ls055592025/")

if movie_page.status_code == 200:
    soup = BeautifulSoup(movie_page.content, "html.parser")
    header_elements = soup.find_all("h3", class_="lister-item-header")

    # List comprehension that finds the titles in all the header_elements
    list_of_titles = [header.find("a").text for header in header_elements]

    # List comprehension that finds the numbers in all the header_elements
    list_of_numbers = [header.find("span", class_="lister-item-index unbold text-primary").text
                       for header in header_elements]

    # Reverse the numbers and movies
    reversed_titles = list_of_titles[::-1]
    reversed_numbers = list_of_numbers[::-1]

    # Final list combined. Used zip which appends multiple lists into a tuple and will write a
    # txt file after putting the space in between each line in final list.
    final_list = []
    for number, title in zip(reversed_numbers, reversed_titles):
        final_list.append(f"{number} {title}")

    # Put a space between each entry in the list.
    with open("Top-100-Movies.txt", "w") as top_movies:
        top_movies.write("\n".join(final_list))

else:
    print(f"Error: {movie_page.status_code} - {movie_page.text}")
