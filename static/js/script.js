const startBtn = document.querySelector('.start-btn');
const popupInfo = document.querySelector('.popup-info');
const exitBtn = document.querySelector('.exit-btn');
const main = document.querySelector('.main');
const continueBtn = document.querySelector('.continue-btn');


//interface pour afficher le score

startBtn.onclick = () => {
    popupInfo.classList.add('active');
    main.classList.add('active');
}

exitBtn.onclick = () => {
    popupInfo.classList.remove('active');
    main.classList.remove('active');
}

continueBtn.onclick = () => {
    popupInfo.classList.remove('active');
    main.classList.remove('active');
   
    
}



const nextBtn = document.querySelector('.next-btn');
const next_btn = document.querySelector('.next-btn')


// revue des questions et options des listes


"########################################################################################################"

//====================================OPTION SELECTED=====================================================

"#########################################################################################################"

