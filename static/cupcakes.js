all_cupcakes = [];
$allcupcakesdiv = $("#allcupcakesdiv");

async function get_cupcakes() {
    all_cupcakes = await axios.get('/api/cupcakes')
    putcupcakesonpage()
    console.log(all_cupcakes)
}

function generateCupcakeMarkup(cupcake) {
    return $(`
    <div class = 'flavor mx-auto my-3 py-auto' id="${cupcake.id} style='width:33.3%'">
    ${cupcake.flavor}
    <div> <img src=${cupcake.image} width= '300' height = '400'></img></div>
    </div>
    `)
}

function putcupcakesonpage() {
    for(let cupcake of all_cupcakes.data) {
        const $cupcake = generateCupcakeMarkup(cupcake)
        console.log($cupcake)
        $allcupcakesdiv.append($cupcake)
    }
}

get_cupcakes()


