document.addEventListener('DOMContentLoaded', () => {
    const carritoDeCompras = document.getElementById('carrito-compras');
    const carritoTotal = document.getElementById('carrito-total');
    const carritoSubtotal = document.getElementById('carrito-subtotal');

    // Variable global para almacenar el subtotal
    let subtotal = 0;
    let total = 0;
    let valorDespacho = 0;

    document.querySelectorAll('.btnAgregarProducto').forEach(button => {
        button.addEventListener('click', (event) => {
            contador = 0;
            contador= parseInt(document.getElementById("carrito-contador").innerText);
            contador = contador + 1;
            document.getElementById("carrito-contador").innerHTML = contador;
            document.getElementById("cantidad-articulos").innerHTML = contador + " Artículo(s)";
            document.getElementById("carrito-contador").classList.remove("visually-hidden");

            const productoCard = event.target.closest('.card.producto');
            const pImagen_src = productoCard.querySelector('.producto-imagen').src;
            const pTitulo_text = productoCard.querySelector('.producto-titulo').innerText;
            const pPrecio_text = productoCard.querySelector('.producto-precio').innerText;
            var pCategoria = "Herramienta";

            // Convierte el precio del producto a número
            const precioNumerico = convertirPrecioANumero(pPrecio_text);

            // Crea el div que corresponde al item del carrito
            const carritoItem = document.createElement('div');
            carritoItem.classList.add('carrito-item', 'row', 'mb-4','d-flex','justify-content-between','align-items-center');
            // Crea la estructura de producto para el carrito
            html_linea = "<hr class='my-4' id='hr-prd-"+contador+"'></hr>";
            html_imagen = "<div class='col-md-2 col-lg-2 col-xl-2 img_producto' id='img-prd-"+contador+"'><img src='"+pImagen_src+"' class='img-fluid rounded-3'></div>";
            html_titulo = "<div class='col-md-6' id='titulo-prd-"+contador+"'><h6 class='text-muted' id='categoria-prd-"+contador+"'>"+pCategoria+"</h6><h6 class='text-black mb-0'>"+pTitulo_text+"</h6></div>";
            html_precio = "<div class='col-md-2' id='precio-prd-"+contador+"'><h6 class='mb-0' >"+pPrecio_text+"</h6></div>";
            html_basurero ="<div class='col-md-1 text-end' id='eliminar-prd-"+contador+"'><button class='eliminar-btn btn btn-light' data-contador='" + contador + "'><i class='bi bi-trash3-fill'></i></button></div>";
            html_item = html_linea+html_imagen+html_titulo+html_precio+html_basurero;
            // Agrega el contenido HTML al item del carrito
            carritoItem.innerHTML = html_item;
            // Agrega el item del carrito como objeto al carrito de compras
            carritoDeCompras.appendChild(carritoItem);

            // Obtiene el subtotal actual del carrito de compras
            contador= parseInt(document.getElementById("carrito-subtotal").innerText);
            document.getElementById("carrito-subtotal").innerHTML = contador;


            // Crea un evento de espera para el boton eliminar item
            carritoItem.querySelector('.eliminar-btn').addEventListener('click', () => {
                carritoDeCompras.removeChild(carritoItem);
                contador= parseInt(document.getElementById("carrito-contador").innerText);
                contador = contador - 1;
                if (contador == 0){
                    document.getElementById("carrito-contador").classList.add("visually-hidden");
                }
                document.getElementById("carrito-contador").innerHTML = contador;
                document.getElementById("cantidad-articulos").innerHTML = contador + " Artículo(s)";
                // Actualizar el subtotal
                subtotal -= precioNumerico;
                actualizarSubtotal(subtotal);
                total = subtotal;
                if(subtotal == 0)
                {
                    total = 0;
                }
                actualizarTotal(total);
            });
            // Actualizar el subtotal
            subtotal += precioNumerico;
            actualizarSubtotal(subtotal);
            total = subtotal;
            actualizarTotal(total);
        });
    });

    function convertirPrecioANumero(precio) {
        // Eliminar caracteres no numéricos excepto los dígitos
        const precioNumerico = parseFloat(precio.replace(/[$.]/g, ''));
        return isNaN(precioNumerico) ? 0 : precioNumerico;
    }

    function actualizarSubtotal(monto) {
        carritoSubtotal.textContent = `$ ${monto.toFixed(0)}`;
    }

    function actualizarTotal(monto) {
        carritoTotal.textContent = `$ ${monto.toFixed(0)}`;
    }
});