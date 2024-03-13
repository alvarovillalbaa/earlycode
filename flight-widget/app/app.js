const departuresBody = document.getElementById('departures-body')


const getFlight = () => {
    fetch('http://localhost:8000/flights')
        .then(response => response.json())
        .then(flights => {
            fillingTable(flights)
        })
        // catching the errors
        .catch(err => console.log(err))
}

getFlight()

const fillingTable = (flights) => {
    console.log(flights)
    // looping through the data array(found through the console)
    for (const flight of flights) {
        const tableRow = document.createElement('tr')
        const tableIcon = document.createElement('td')
        tableIcon.textContent = '+'
        tableRow.append(tableIcon)

        const flightDetails = {
            time: flight.dep_time.slice(0, 5), // to only return 5 values to display
            destination: flight.dep_iata.toUpperCase(),
            flight: flight.flight_number.shift(), // to return only the first value
            gate: flight.dep_gate,
            remarks: flight.status,
        }

        for (const flightDetail in flightDetails) {
            const tableCell = document.createElement('td')
            const word = Array.from(flightDetails[flightDetail])

            for (const [index, letter] of word.entries()) {
                const letterElement = document.createElement('div')

                letterElement.textContent = letter

                tableCell.append(letterElement)
            }
            tableRow.append(tableCell)
        }

        departuresBody.append(tableRow)
    }

}