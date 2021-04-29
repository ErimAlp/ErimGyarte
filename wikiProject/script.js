import {getwebquote} from './fetchquotes';

addlisteners();

function addlisteners() {
    document.querySelector('button').addEventListener('click', quoteButtonClicked);
}

function quoteButtonClicked() {
    getwebquote().then( insertparagraph);
   
}

function insertparagraph(text){
    const p = document.createElement('p');
        p.innerText ='Philip rekommenderar: ' + text[0];
    document.querySelector('body').appendChild(p);

    const img =  document.createElement("img");
    img.setAttribute("src", text[1])
    document.querySelector('body').appendChild(img)
}
