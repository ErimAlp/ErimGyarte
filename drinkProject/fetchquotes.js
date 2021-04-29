export function getwebquote(){

   return fetch("https://www.thecocktaildb.com/api/json/v1/1/random.php")
    .then(function (response) {
        return response.json();
    })
    .then(function (data){
        var name = data.drinks[0].strDrink
        var picture = data.drinks[0].strDrinkThumb
        
        console.log(data.drinks[0].strDrink)
        return [name, picture]
    });
}