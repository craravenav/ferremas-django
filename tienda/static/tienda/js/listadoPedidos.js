// Iniciador de alerta Toast para descarga de PDF
const toastLive = document.getElementById('ToastDescarga')
const downloadBtns = document.querySelectorAll('.downloadBtn')

Array.from(downloadBtns).forEach(button => {
    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLive)
    button.addEventListener('click', () => {
        toastBootstrap.show()
        setTimeout(() =>{
            window.open("docs/Ferremas-ordendecompra.pdf","_blank")
        },5000);
    })
})

// Iniciador de tooltips Bootstrap5
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

// Iniciador de alerta toast de confirmación de acción
const toastConfirm = document.getElementById('ToastConfirmaRechazo')
const toastConfirmBtn = document.getElementById('BtnConfirmaRechazo')

if (toastConfirmBtn) {
    const toastBootstrap2 = bootstrap.Toast.getOrCreateInstance(toastConfirm)
    toastConfirmBtn.addEventListener('click', () => {
      toastBootstrap2.show()
    })
  }


  