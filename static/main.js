function fetchOrderBook() {
    fetch("/orderbook_data")
        .then(response => response.json())
        .then(data => {
            updateTable(data);
        })
        .catch(error => {
            console.error("Error:", error);
        });
}


function updateTable(data) {
    const tableBodyA = document.getElementById("orderbook-body-bids");
    const tableBodyB = document.getElementById("orderbook-body-asks");


    tableBodyA.innerHTML = "";
    tableBodyB.innerHTML = "";


    data.bids.forEach(row => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td style="color: green;">${row[0]}</td>
            <td>${row[1]}</td>
            <td style="color: green;">Bid</td>
        `;
        tableBodyA.appendChild(tr);
    });

    data.asks.forEach(row => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td style="color: red;">${row[0]}</td>
            <td>${row[1]}</td>
            <td style="color: red;">Ask</td>
        `;
        tableBodyB.appendChild(tr);
    });
}


setInterval(() => {
    fetchOrderBook();
}, 2000);

document.getElementById("symbol-select").addEventListener("change", () => {
    console.log("Symbol changed (placeholder)");
});


