export default function initCadastro(){
    const tabMenu = document.querySelectorAll('[data-tab="menu"] li')
    const tabContent = document.querySelectorAll('[data-tab="content"] li')
    
    if(tabMenu.length && tabContent.length) {
        tabContent[0].classList.add('ativo')
        
        function activeTab(index){
            tabContent.forEach((lista) =>{
                lista.classList.remove('ativo')
            });
            const direcao = tabContent[index].dataset.anime
            tabContent[index].classList.add('ativo', direcao);
        }
        
        tabMenu.forEach((itenMenu, index) =>{
            itenMenu.addEventListener('click', () => {
                activeTab(index)
            })
        })
    }
}

