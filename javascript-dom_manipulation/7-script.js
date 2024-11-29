document.addEventListener("DOMContentLoaded", () => {
	const url = "https://swapi-api.hbtn.io/api/films/?format=json";

	// Fetch the movie data
	fetch(url)
		.then((response) => {
			if (!response.ok) {
				throw new Error(`HTTP error! status: ${response.status}`);
			}
			return response.json();
		})
		.then((data) => {
			const movies = data.results; // Array of movie objects
			const movieList = document.getElementById("list_movies");

			// Loop through the movies and create list items
			movies.forEach((movie) => {
				const listItem = document.createElement("li");
				listItem.textContent = movie.title;
				movieList.appendChild(listItem);
			});
		})
		.catch((error) => {
			console.error("Error fetching movie data:", error);
		});
});
