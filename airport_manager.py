######################## IMPORTANT ########################
""" Do not rename the variables or functions.
Do not change the function parameters.
Do not add input() calls inside airport_manager.py.
The file must be importable by the tests. """
###########################################################


airport_info = (
    "OUL",
    1,
    "14-09-2026"
)

allowed_gates = {
    "A1",
    "A2",
    "A3",
    "A4",
    "B1",
    "B2"
}

restricted_destinations = {
    "Moscow",
    "Pyongyang"
}

flights = {
    "AY450": {
        "destination": "Helsinki",
        "departure": "08:30",
        "gate": "A2",
        "capacity": 5,
        "passengers": [
            "Alice Wong",
            "David Kim",
            "Fatima Ali"
        ]
    },
    "SK271": {
        "destination": "Stockholm",
        "departure": "10:15",
        "gate": "B1",
        "capacity": 4,
        "passengers": [
            "Chen Wei",
            "George Smith"
        ]
    },
    "LH2491": {
        "destination": "Munich",
        "departure": "12:40",
        "gate": "A4",
        "capacity": 5,
        "passengers": [
            "Hana Lee",
            "Maria Garcia",
            "Noah Wilson"
        ]
    }
}


## Logic to find if a flight exists
def find_flight(flights, flight_number):
    flight_number = flight_number.strip().upper()

    if flight_number in flights:
        return flight_number

    return None


## Logic to find if a passenger exists
def passenger_exists(passengers, passenger_name):
    passenger_name = passenger_name.strip().lower()

    for passenger in passengers:
        if passenger.strip().lower() == passenger_name:
            return True

    return False


## Logic to check in a passenger
def check_in_passenger(
    flights,
    flight_number,
    passenger_name,
    restricted_destinations
):
    flight_key = find_flight(flights, flight_number)

    if flight_key is None:
        return "FLIGHT_NOT_FOUND"

    passenger_name = passenger_name.strip()

    if passenger_name == "":
        return "EMPTY_NAME"

    passenger_name = passenger_name.title()
    flight = flights[flight_key]

    if passenger_exists(flight["passengers"], passenger_name):
        return "DUPLICATE"

    if len(flight["passengers"]) >= flight["capacity"]:
        return "FULL"

    if flight["destination"] in restricted_destinations:
        return "RESTRICTED"

    flight["passengers"].append(passenger_name)
    return "OK"


## Logic to remove a passenger from a flight
def remove_passenger(
    flights,
    flight_number,
    passenger_name
):
    flight_key = find_flight(flights, flight_number)

    if flight_key is None:
        return "FLIGHT_NOT_FOUND"

    passenger_name = passenger_name.strip().lower()
    passengers = flights[flight_key]["passengers"]

    for index in range(len(passengers)):
        if passengers[index].strip().lower() == passenger_name:
            passengers.pop(index)
            return "OK"

    return "PASSENGER_NOT_FOUND"


# Logic to change the gate of a flight
def change_gate(
    flights,
    flight_number,
    new_gate,
    allowed_gates
):
    flight_key = find_flight(flights, flight_number)

    if flight_key is None:
        return "FLIGHT_NOT_FOUND"

    new_gate = new_gate.strip().upper()

    if new_gate not in allowed_gates:
        return "INVALID_GATE"

    flights[flight_key]["gate"] = new_gate
    return "OK"


# Logic to get the status of a flight
def flight_status(flight):
    capacity = flight["capacity"]
    passenger_count = len(flight["passengers"])

    if capacity <= 0:
        return "FULL"

    percentage = passenger_count / capacity * 100

    if percentage >= 100:
        return "FULL"
    elif percentage >= 75:
        return "ALMOST FULL"
    else:
        return "AVAILABLE"


# Logic to get the sorted manifest of a flight
def sorted_manifest(
    flights,
    flight_number
):
    flight_key = find_flight(flights, flight_number)

    if flight_key is None:
        return None

    return sorted(flights[flight_key]["passengers"])


# Logic to get the total number of passengers across all flights
def total_passengers(flights):
    total = 0

    for flight in flights.values():
        total += len(flight["passengers"])

    return total


# Logic to check if any flight is full
def any_full_flight(flights):
    for flight in flights.values():
        if len(flight["passengers"]) >= flight["capacity"]:
            return True

    return False


# Logic to check if all flights have at least one passenger
def all_flights_have_passengers(flights):
    for flight in flights.values():
        if len(flight["passengers"]) == 0:
            return False

    return True