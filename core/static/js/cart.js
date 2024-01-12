function addToCart(product_id) {
    console.log(product_id)
    $.ajax({
        url: "{%  url 'cart:session-add-product' %}",
        method: 'POST',
        data: {
            product_id: product_id,
            csrfmiddlewaretoken: '{{ csrf_token }}'

        },
        success: function (response) {
            console.log(response);
            // do something with the response data
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(errorThrown);
            // handle the error case
        }
    });
}