const backendURL = "http://3.232.46.241:8000/api"; // ✅ Replace with your actual EC2 API URL


// Book a Ride
document.getElementById("bookingForm")?.addEventListener("submit", function(event) {
    event.preventDefault();

    let customerName = document.getElementById("customerName").value;
    let customerEmail = document.getElementById("customerEmail").value;
    let customerPhone = document.getElementById("customerPhone").value;
    let pickup = document.getElementById("pickup").value;
    let drop = document.getElementById("drop").value;

    // Step 1: Create Customer with Email & Phone
    fetch(`${backendURL}/customers/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            name: customerName,
            email: customerEmail,
            phone: customerPhone
        })
    })
    .then(response => response.json())
    .then(customerData => {
        if (customerData.id) {
            let customerId = customerData.id;  // ✅ Get customer ID

            // Step 2: Book Ride with Customer ID
            return fetch(`${backendURL}/rides/`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    customer: customerId,
                    pickup_location: pickup,
                    drop_location: drop,
                    ride_status: "Pending"
                })
            });
        } else {
            throw new Error("Customer creation failed: " + JSON.stringify(customerData));
        }
    })
    .then(response => {
        if (!response.ok) throw new Error("Ride booking failed");
        return response.json();
    })
    .then(data => {
        document.getElementById("bookingResult").innerText = "✅ Ride booked successfully!";
    })
    .catch(error => console.error("❌ Error:", error));
});

// ✅ Fetch Ride History with Filtering
function fetchRideHistory(filterStatus = "") {
    fetch(`${backendURL}/rides/`)
    .then(response => response.json())
    .then(data => {
        let tableBody = document.getElementById("rideHistory");
        tableBody.innerHTML = ""; // Clear previous data

        if (data.length === 0) {
            tableBody.innerHTML = "<tr><td colspan='3'>No rides available</td></tr>";
            return;
        }

        data.forEach(ride => {
            if (!filterStatus || ride.ride_status === filterStatus) {
                let row = `<tr>
                    <td>${ride.pickup_location}</td>
                    <td>${ride.drop_location}</td>
                    <td>${ride.ride_status}</td>
                </tr>`;
                tableBody.innerHTML += row;
            }
        });
    })
    .catch(error => console.error("Error fetching ride history:", error));
}

// ✅ Filter Ride History on Status Change
document.getElementById("statusFilter")?.addEventListener("change", function() {
    fetchRideHistory(this.value);
});

// ✅ Call fetchRideHistory when the history page loads
if (document.getElementById("rideHistory")) {
    fetchRideHistory();
}


// Calculate Fare
function calculateFare() {
    let distance = document.getElementById("distance").value;

    fetch(`${backendURL}/calculate-fare/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ distance_km: distance })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("fareResult").innerText = `Estimated Fare: $${data.fare}`;
    })
    .catch(error => console.error("Error:", error));
};