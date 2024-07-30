// // categories loading button logic

// // explore loading button logic
// document.addEventListener('DOMContentLoaded', () => {

//   const exploreMore = document.querySelector('.explore-more');


//   if (exploreMore) {
//     let currentItems = 8;

//     exploreMore.addEventListener('click', (e) => {
//       e.preventDefault();
//       console.log('clicado')
//       const elementList = [...document.querySelectorAll('.explore-item')];
//       e.target.classList.add('show-loader');

//       for (let i = currentItems; i < currentItems + 8; i++) {
//         setTimeout(function () {
//           e.target.classList.remove('show-loader');

//           if (elementList[i]) {
//             elementList[i].style.display = 'flex';
//           }
//         }, 3000)
//       }
//       currentItems += 8;

//       // hide load button after fully load items
//       if (currentItems >= elementList.length) {
//         event.target.classList.add('loaded')
//       }

//     })
//   }



//   const categoryMore = document.querySelector('.category-more');
//   const totalCategories = document.querySelector('.total-categories');


//   if (categoryMore) {
//     let currentCategoryItems = 8

//     categoryMore.addEventListener('click', (e) => {
//       e.preventDefault();
//       const elementList = [...document.querySelectorAll('.categories-row-item')];
//       e.target.classList.add('show-loader');

//       for (let i = currentCategoryItems; i < currentCategoryItems + 8; i++) {
//         setTimeout(function () {
//           e.target.classList.remove('show-loader');

//           if (elementList[i]) {
//             elementList[i].style.display = 'flex';
//           }
//         }, 3000)
//       }
//       currentCategoryItems += 8;

//       // hide load button after fully load items
//       if (currentCategoryItems >= elementList.length) {
//         event.target.classList.add('loaded')
//       }

//     })
//   }
// });


document.addEventListener('DOMContentLoaded', () => {
  // explore loading button logic
  const exploreMore = document.querySelector('.explore-more');
  if (exploreMore) {
    let currentExploreItems = 8;

    exploreMore.addEventListener('click', (e) => {
      e.preventDefault();
      console.log('Explore button clicked');
      const elementList = [...document.querySelectorAll('.explore-item')];
      e.target.classList.add('show-loader');

      for (let i = currentExploreItems; i < currentExploreItems + 8; i++) {
        setTimeout(function () {
          e.target.classList.remove('show-loader');

          if (elementList[i]) {
            elementList[i].style.display = 'flex';
          }
        }, 3000);
      }
      currentExploreItems += 8;

      // hide load button after fully load items
      if (currentExploreItems >= elementList.length) {
        e.target.classList.add('loaded');
      }
    });
  } else {
    console.error('Button .explore-more not found');
  }

  // categories loading button logic
  const categoryMore = document.querySelector('.category-more');
  if (categoryMore) {
    let currentCategoryItems = 8;

    categoryMore.addEventListener('click', (e) => {
      e.preventDefault();
      console.log('Category button clicked');
      const elementList = [...document.querySelectorAll('.categories-row-item')];
      e.target.classList.add('show-loader');

      for (let i = currentCategoryItems; i < currentCategoryItems + 8; i++) {
        setTimeout(function () {
          e.target.classList.remove('show-loader');

          if (elementList[i]) {
            elementList[i].style.display = 'flex';
          }
        }, 3000);
      }
      currentCategoryItems += 8;

      // hide load button after fully load items
      if (currentCategoryItems >= elementList.length) {
        e.target.classList.add('loaded');
      }
    });
  } else {
    console.error('Button .category-more not found');
  }
});
