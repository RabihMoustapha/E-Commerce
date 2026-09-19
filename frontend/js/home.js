function loadProducts() {
    fetch('../../backend/products.py')
        .then(response => response.json())
        .then(data => {
            const productsContainer = document.getElementById('products-container');

            // Clear existing products
            productsContainer.innerHTML = '';
        })
}