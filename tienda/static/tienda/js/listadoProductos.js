const ModalProducto = document.getElementById('ModalProducto')
if (ModalProducto) {
    ModalProducto.addEventListener('show.bs.modal', event => {
    // Button that triggered the modal
    const button = event.relatedTarget
    // Extrae los datos de cada linea de la tabla segun el boton
    const productoNombre = button.getAttribute('data-producto-nombre')
    const productoMarca = button.getAttribute('data-producto-marca')
    const productoImagen = button.getAttribute('data-producto-imagen')
    const productoPrecio = button.getAttribute('data-producto-precio')

    // Asigna los valores obtenidos del boton
    const modalProductoNombre = ModalProducto.querySelector('.producto-nombre')
    const modalProductoMarca = ModalProducto.querySelector('.producto-marca')
    const modalProductoPrecio = ModalProducto.querySelector('.producto-precio')
    const modalProductoImagen = ModalProducto.querySelector('.producto-imagen')

    modalProductoNombre.textContent = productoNombre;
    modalProductoMarca.textContent = productoMarca;
    modalProductoPrecio.textContent = productoPrecio;
    modalProductoImagen.setAttribute('src', productoImagen);
  })
}