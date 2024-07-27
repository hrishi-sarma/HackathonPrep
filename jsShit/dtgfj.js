let query = document.querySelector('.query');
let searchButton = document.querySelector('.go')

searchButton.onclick = function(){
    let url =  'https://www.google.com/search?q=' +query.value;
    window.open(url, '_self');}