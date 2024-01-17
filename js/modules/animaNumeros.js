export default function initAnimaNumeros(){
    const numeros = document.querySelectorAll('p');  
    const arrayNumeros = Array.from(numeros);
    
    function aumentaFont() {
        arrayNumeros.forEach((element) => {
            element.setAttribute('class', 'fs-4 user-select-none');
        });
    }
    aumentaFont();
}

const background = document.querySelector('section')
background.setAttribute('id', 'info')
