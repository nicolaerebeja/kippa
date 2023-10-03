const autoCompleteJS = new autoComplete({
    selector: "#autoComplete",
    customClass: 'form-control w-100',
    data: {
        src: async (query) => {
            try {
                // Fetch Data from external Source
                const source = await fetch(`/api/cerca-clienti?q=${query}`);
                // Data should be an array of `Objects` or `Strings`
                const data = await source.json();

                return data;
            } catch (error) {
                return error;
            }
        },
        // Data source 'Object' key to be searched
        keys: ["ragioneSociale"]
    },
    resultsList: {
        element: (list, data) => {
            if (!data.results.length) {
                // Create "No Results" message element
                const message = document.createElement("div");
                // Add class to the created element
                message.setAttribute("class", "no_result");
                // Add message text content
                message.innerHTML = `<span>Found No Results for "${data.query}"</span>`;
                // Append message element to the results list
                list.prepend(message);
            }
        },
        noResults: true,
    },
    resultItem: {
        highlight: true
    },
    events: {
        input: {
            selection: (event) => {
                clt = event.detail.selection.value;
                const selection = clt.ragioneSociale
                autoCompleteJS.input.value = selection;
                const sede = clt.via + ', ' + clt.comune + ' ' + clt.provincia;
                document.getElementsByName('sede')[0].value = sede
                document.getElementById('id').value = clt.id
            }
        }
    }
});
document.getElementById('autoComplete').parentElement.className = 'input-group input-group-dynamic'



var inputs = document.getElementsByTagName('input');
for (let i = 0; i < inputs.length; i++) {
    var val = inputs[i].value
    if (val.length > 1) {
        inputs[i].parentElement.className = "input-group input-group-dynamic is-filled"
    }
}





const urlParams = new URLSearchParams(window.location.search);
const clienteId = urlParams.get('cliente');

if (clienteId && clienteId.trim() !== '') {
    document.getElementById('autoComplete').value = clienteId
}