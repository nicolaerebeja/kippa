
function editProfile() {
    var form = document.getElementById('ang_cliente');
    var inputs = form.querySelectorAll('input');

    for (var i = 0; i < inputs.length; i++) {
        inputs[i].disabled = false;
    }

    document.getElementById('startEditProfile').hidden = true

    var div = document.getElementById('editProfile');

    var buttonSave = document.createElement('button');
    buttonSave.setAttribute('id', 'buttonSave');
    buttonSave.setAttribute('type', 'submit');
    buttonSave.setAttribute('class', 'btn btn-sm btn-success me-2');
    buttonSave.innerHTML = 'Salva';

    var buttonCancel = document.createElement('button');
    buttonCancel.setAttribute('id', 'buttonCancel');
    buttonCancel.setAttribute('type', 'button');
    buttonCancel.setAttribute('class', 'btn btn-sm btn-warning');
    buttonCancel.innerHTML = 'Cancel';

    div.appendChild(buttonSave);
    div.appendChild(buttonCancel);

    document.getElementById('buttonCancel').onclick = cancelForm

    function cancelForm() {
        var elem = document.getElementById('buttonSave');
        elem.parentNode.removeChild(elem);
        var elem = document.getElementById('buttonCancel');
        elem.parentNode.removeChild(elem);

        document.getElementById('startEditProfile').hidden = false

        return false;
    }
}

function welcomeMail() {
    Swal.fire({
        title: 'Sei sicuro?',
        html: "Stai per inviare l'email di benvenuto al cliente:<br>"+ragionesociale+" / "+email+"",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, invia!'
    }).then((result) => {
        if (result.isConfirmed) {
            fetch('/invia-mail', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        email: [email],
                        id: [idCliente],
                        type: 'mail_di_presentazione',
                    })
                })
                .then(response => response.json())
                .then(data => {

                    console.log(data);
                    Swal.fire(
                        'Inviato!',
                        "L'email è stata inviata con successo!",
                        'success'
                    )

                })
                .catch(error => {
                    console.error(error);
                });
        }
    })
}


function censimentoMail() {
    Swal.fire({
        title: 'Sei sicuro?',
        html: "Stai per inviare l'email di censimento al cliente:<br>"+ragionesociale+" / "+email+"",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, invia!'
    }).then((result) => {
        if (result.isConfirmed) {
            fetch('/invia-mail', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        email: [email],
                        id: [idCliente],
                        type: 'mail_di_censimento',
                    })
                })
                .then(response => response.json())
                .then(data => {

                    console.log(data);
                    Swal.fire(
                        'Inviato!',
                        "L'email è stata inviata con successo!",
                        'success'
                    )

                })
                .catch(error => {
                    console.error(error);
                });
        }
    })
}


function invioPinMail() {
    let pinEmail = document.getElementById('pinEmail').value;
    let body = quill.root.innerHTML;
    Swal.fire({
        title: 'Sei sicuro?',
        html: "Stai per inviare il pin al cliente:<br>"+ragionesociale+" / "+pinEmail+"",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, invia!'
    }).then((result) => {
        if (result.isConfirmed) {
            fetch('/invia-mail', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        email: [pinEmail],
                        id: [idCliente],
                        type: 'mail_pin',
                        body: body
                    })
                })
                .then(response => response.json())
                .then(data => {

                    console.log(data);
                    Swal.fire(
                        'Inviato!',
                        "L'email è stata inviata con successo!",
                        'success'
                    )

                })
                .catch(error => {
                    console.error(error);
                });
        }
    })
}


// Initialize Dialog jQuery UI
$(function() {
    $("#my-dialog").dialog({
        autoOpen: false,
        draggable: true,
        modal: true,
        width: 700,
        title: "Modulo Invio Pin",
        buttons: {
            "Invia": function() {
                invioPinMail();
            },
            "Annulla": function() {
                $(this).dialog("close");
            }
        }
    });

    $("#pinmail").on("click", function() {
        $("#my-dialog").dialog("open");
    });
});

// Initialize Quill editor
var quill = new Quill('#editor', {
    theme: 'snow'
});