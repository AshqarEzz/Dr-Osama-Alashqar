function searchFunction() {
    // Get the text typed in the search bar
    let input = document.getElementById('searchBar').value.toLowerCase();
    // Get all the cards on the current page
    let cards = document.getElementsByClassName('card');

    for (let i = 0; i < cards.length; i++) {
        // Look at the title (h3) inside each card
        let title = cards[i].getElementsByTagName('h3')[0].innerText.toLowerCase();
        
        // If the title matches the search, show it. Otherwise, hide it.
        if (title.includes(input)) {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        }
    }
}