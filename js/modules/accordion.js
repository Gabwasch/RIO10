export default function initAccordion(){
    const accordionList = document.querySelectorAll('[data-anime="accordion"] dt')
    const activeClass = 'ativo';
    if(accordionList.length){
        function activeAccordion(){
            this.classList.toggle(activeClass)
            this.nextElementSibling.classList.toggle(activeClass)
        }
        accordionList.forEach((item) => {
            item.classList.remove('ativo')
            item.addEventListener('click', activeAccordion);
        })
    }
}