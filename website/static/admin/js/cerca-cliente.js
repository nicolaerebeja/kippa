const autoCompleteJS = new autoComplete({
    selector: "#autoComplete",
    // customClass: 'form-control w-100',
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
        cache: true,

        keys: ["ragioneSociale","linkAccount", "referente", "codiceCliente", "idPath", "telefono", "piva", ]
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
                const selection = event.detail.selection.value.id;
                var url = '/cliente/'+selection;
                //window.location.href=url;
                window.open(url, '_blank').focus();
            }
        }
    }
});
document.getElementById('autoComplete').parentElement.className = 'input-group input-group-dynamic'


