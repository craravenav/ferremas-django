(() => {
    'use strict'
  
    // Busca todos los forms en los que se quiera aplicar validaciones de Bootstrap
    const forms = document.querySelectorAll('.needs-validation')
  
    // Recorre todos los formularios seleccionados en el paso anterior y valida 
    // ante el evento Submit del formulario interrumpiendo la ejecución
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        // CheckValidity es un metodo de HTML que retorna true si el elemento no tiene problemas de validación de lo contrario retorna invalid
        if (!form.checkValidity()) {
          // Metodo de la interfaz Event del DOM que permite controlar el funcionamiento del evento en este caso si es cancelable, lo cancela pero no detiene el funcionamiento restante
          event.preventDefault()
          // Metodo de la Interfaz Event del DOM que permite controlar la propagación hacia los selectores externos sobre el cual se está ejecutando el evento.
          event.stopPropagation()
        }
        
        // En caso de validarse correctamente se le agrega la clase was-validated
        form.classList.add('was-validated')
      }, false)
    })
    
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
  })()