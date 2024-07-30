const productBigImage = document.getElementById('productBigImage');
const productSmallImage1 = document.getElementById('productSmallImage1');
const productSmallImage2 = document.getElementById('productSmallImage2');
const productSmallImage3 = document.getElementById('productSmallImage3');
const productSmallImage4 = document.getElementById('productSmallImage4');


productSmallImage1.addEventListener('click', () => {
  console.log('clicado')
  productBigImage.src = `${productSmallImage1.src}`
});

productSmallImage2.addEventListener('click', () => {
  productBigImage.src = `${productSmallImage2.src}`
});

productSmallImage3.addEventListener('click', () => {
  productBigImage.src = `${productSmallImage3.src}`
});

productSmallImage4.addEventListener('click', () => {
  productBigImage.src = `${productSmallImage4.src}`
});