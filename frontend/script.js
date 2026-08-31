const API_URL = "http://127.0.0.1:8000";

const API_KEY = "smartexpense-key";


async function loadExpenses() {

    const response =
        await fetch(`${API_URL}/expenses`);

    const expenses =
        await response.json();


    const container =
        document.getElementById("expenses");


    container.innerHTML = "";


    expenses.forEach(expense => {

        const div =
            document.createElement("div");

        div.className = "expense";

        div.innerHTML = `
            <strong>${expense.title}</strong>
            <p>₹${expense.amount}</p>
            <p>Category: ${expense.category}</p>
            <p>${expense.description || ""}</p>
        `;

        container.appendChild(div);

    });


    loadSummary();
}


async function loadSummary() {

    const response =
        await fetch(`${API_URL}/summary`);

    const data =
        await response.json();


    document.getElementById("total")
        .innerText =
        `₹${data.total_amount}`;


    document.getElementById("count")
        .innerText =
        data.total_expenses;
}


async function addExpense() {

    const expense = {

        title:
            document.getElementById("title").value,

        amount:
            Number(
                document.getElementById("amount").value
            ),

        category:
            document.getElementById("category").value,

        description:
            document.getElementById("description").value

    };


    await fetch(
        `${API_URL}/expenses`,
        {

            method: "POST",

            headers: {

                "Content-Type":
                    "application/json",

                "X-API-Key":
                    API_KEY

            },

            body:
                JSON.stringify(expense)

        }
    );


    document.getElementById("title").value = "";

    document.getElementById("amount").value = "";

    document.getElementById("category").value = "";

    document.getElementById("description").value = "";


    loadExpenses();
}


loadExpenses();