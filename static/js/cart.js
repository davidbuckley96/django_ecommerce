var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('the product id:', productId, '; the action:', action)

        console.log('the user:', user)
        if (user == 'AnonymousUser') {
            console.log('User is not authenticated')
        } else {
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action) {
    console.log('User is authenticated')

    var url = '/update-item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action
        })
    })

        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data:', data)

            updateCartUI(data.total_cart_quantity, data.order_items_count, data.order_item_quantity, data.order_item_price, data.product_id, data.cart_total_price);
            console.log('Quantity changed successfully')
        })

        .catch(error => {
            console.error('Error changing quantity', error);
        })
}


function updateCartUI(totalCartQuantity, orderItemsCount, orderItemQuantity, orderItemPrice, productId, cartTotalPrice) {
    var cartQuantitySpan = document.getElementById('cart-quantity');
    if (cartQuantitySpan) {
        cartQuantitySpan.innerText = totalCartQuantity
    }

    var totalCartQuantitySpan = document.getElementById('total-cart-quantity');
    if (totalCartQuantitySpan) {
        totalCartQuantitySpan.innerText = totalCartQuantity
    }

    var orderItemTotalSpan = document.getElementById('order-items-total');
    if (orderItemTotalSpan) {
        orderItemTotalSpan.innerText = orderItemPrice
    }

    var orderItemQuantitySpan = document.getElementById('order-items-count');
    if (orderItemQuantitySpan) {
        orderItemQuantitySpan.innerText = orderItemQuantity
    }

    var orderTotalSpan = document.getElementById('cart-total');
    if (orderTotalSpan) {
        orderTotalSpan.innerText = cartTotalPrice
    }

    if (orderItemQuantity < 1) {
        var productElement = document.getElementById(productId)
        console.log('o elemento é', productElement)
        if (productElement) {
            productElement.remove();
        }
    }
}