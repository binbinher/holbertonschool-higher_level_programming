document.addEventListener("DOMContentLoaded", () => {
	const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";

	// Fetch the character data
	fetch(url)
		.then((response) => {
			if (!response.ok) {
				throw new Error(`HTTP error! status: ${response.status}`);
			}
			return response.json();
		})
		.then((data) => {
			// Extract and display the character name
			document.getElementById("character").textContent = data.name;
		})
		.catch((error) => {
			console.error("Error fetching character data:", error);
		});
});
