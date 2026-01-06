function goToPlace(place) {
    window.location.href = place+".html";
}

let saveFile = () => {
    var rd1 = document.getElementById("rd1");
    var rd2 = document.getElementById("rd2");
    if(rd1.checked==true)
        var pandemic = rd1.value;
    else if(rd2.checked==true)
        var pandemic = rd2.value;

    const email = document.getElementById("txtEmail").value;
    const travel = document.getElementById("txtTravel").value;
    const province = document.getElementById("selProvince").value;
    const airport = document.getElementById("selAirport").value;
    const msg = document.getElementById("msg").value;

    let missingFields = [];

    if (!email) {
        missingFields.push("Email");
    }

    if (!travel) {
        missingFields.push("How many flights do you take annually?");
    }

    if (!rd1.checked && !rd2.checked) {
        missingFields.push("Did you use air travel during the COVID-19 Pandemic?");
    }

    if (province === "-- Choose your province --") {
        missingFields.push("Province");
    }

    if (airport === "-- Preferred Airport For Air Travel --") {
        missingFields.push("Preferred Airport");
    }

    if (!msg) {
        missingFields.push("Reason for choosing airport");
    }

    if (missingFields.length > 0) {
        alert("Please fill in the following fields: \n" + missingFields.join(", "));
        return;
    }

    let data = {
        Email: email,
        Flights: travel,
        Pandemic: pandemic,
        Province: province,
        Airport: airport,
        Message: msg
    };
    
    let savedData = localStorage.getItem("formData");
    let formData = savedData ? JSON.parse(savedData) : [];
    
    formData.push(data);
    localStorage.setItem("formData", JSON.stringify(formData));
    console.log("Data saved:", formData);
    
    displayEntries();
    document.getElementById("surveyForm").reset();
};
    
let displayEntries = () => {
    let savedData = localStorage.getItem("formData");
    let displayArea = document.getElementById("displayArea");
    
    if (savedData) {
        try {
            let formData = JSON.parse(savedData);
    
            let displayText = "";
            formData.forEach(entry => {
                for (const key in entry) {
                    displayText += `${key}: ${entry[key]}\n`;
                }
                displayText += "\n";
            });

            if (displayArea) {
                displayArea.value = displayText;
            }

        } catch (error) {
            console.error("Error parsing JSON:", error);
            if (displayArea) {
                displayArea.value = "Error retrieving data.";
            }
        }
    } else {
        if (displayArea) {
            displayArea.value = "No entries yet.";
        }
    }
};
    
displayEntries();

window.onload = displayEntries;

function clearStorage() {
    localStorage.clear();
}
/* CONTINUE IF I HAVE TIME
function calculatePandemic() {
    let savedData = localStorage.getItem("formData");
    let yesCount = 0;
    let noCount = 0;

    if (savedData) {
        try {
            let formData = JSON.parse(savedData);
            formData.forEach(entry => {
                if (entry.Pandemic === "Yes") {
                    yesCount++;
                } else if (entry.Pandemic === "No") {
                    noCount++;
                }
            });
        } catch (error) {
            console.error("Error parsing JSON:", error);
        }
    }
    return { yes: yesCount, no: noCount };
}

document.addEventListener('DOMContentLoaded', function() {
    let counter = calculatePandemic();

    let yesCounter = document.getElementById("pandemicYes");
    let noCounter = document.getElementById("pandemicNo");

    if (yesCounter) {
        yesCounter.textContent = `Number of "Yes" responses: ${counter.yes}`;
    } else {
        console.error("Element to display 'yes' count not found!");
    }

    if (noCounter) {
        noCounter.textContent = `Number of "No" responses: ${counter.no}`;
    } else {
        console.error("Element to display 'no' count not found!");
    }
});
*/
