function buttonSelect(button, containerClass, buttonClass) {
    var container = button.closest(`${containerClass}`);
    var form = container.querySelector('form');
    var inactiveButton = container.querySelector(`.${buttonClass}.inactive`);
    var activeButton = container.querySelector(`.${buttonClass}.active`);
    console.log(inactiveButton, activeButton)

    if (button.classList.contains('inactive')) {
        inactiveButton.classList.replace('inactive', 'active');
        activeButton.classList.replace('active', 'inactive');
    }

    if (form.classList.contains('hidden')) {
        form.classList.remove('hidden');
    }
}

// function shippingButtonSelect(button) {
//     var container = button.closest('.shipping-info');
//     // var form = container.querySelector('form');
//     var inactiveButton = container.querySelector('.shipping-button.inactive');
//     var activeButton = container.querySelector('.shipping-button.active');

//     if (button.classList.contains('inactive')) {
//         inactiveButton.classList.replace('inactive', 'active');
//         activeButton.classList.replace('active', 'inactive');
//     }
// }

// function billingButtonSelect(button) {
//     var container = button.closest('.billing-info');
//     // var form = container.querySelector('form');
//     var inactiveButton = container.querySelector('.billing-button.inactive');
//     var activeButton = container.querySelector('.billing-button.active');

//     if (button.classList.contains('inactive')) {
//         inactiveButton.classList.replace('inactive', 'active');
//         activeButton.classList.replace('active', 'inactive');
//     }
// }

function toggleForm(button) {
    var form = button.parentElement.nextElementSibling;

    if (button.classList.contains('inactive')) {
        button.classList.replace('inactive', 'active');
        form.classList.remove('hidden')
    }
    else {
        button.classList.replace('active', 'inactive');
        form.classList.add('hidden')
    }
}

function paymentFormToggle(button) {
    var container = button.closest('.payment-method');
    var form = container.querySelector('form');

    if (button.classList.contains('inactive')) {
        button.classList.replace('inactive', 'active');
        form.classList.remove('hidden');
    } else {
        button.classList.replace('active', 'inactive');
        form.classList.add('hidden');
    }
}