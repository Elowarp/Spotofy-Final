var searchInput = document.getElementById("search")
searchInput.addEventListener('keydown', (event) => {
    if (event.key === "Enter"){
        window.location.replace("/search?q=" + searchInput.value)
    }
    
})