const favoriteBar = document.getElementById('favorite-bar')

function renderFavedIcon(){
    console.log(favoriteBar)
    if (favoriteBar.style.display === 'none') {
        favoriteBar.style.display = ""
        favoriteBar.style.display = 'block';
    } else {
        favoriteBar.style.display = 'none';
    } 
}