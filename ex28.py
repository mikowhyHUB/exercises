"""Functions which helps the locomotive engineer to keep track of the train."""


# TODO: define the 'get_list_of_wagons' function
def get_list_of_wagons(numbers):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    # for i in numbers:
    #     print(i)
    return [list(num) for num in numbers]


# TODO: define the 'fixListOfWagons()' function


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """

    a, b, c, *rest = each_wagons_id
    each_wagons_id = rest + [a, b]
    outcome = *missing_wagons, *each_wagons_id
    return [c]+list(outcome)


# TODO: define the 'add_missing_stops()' function
def add_missing_stops(route, stop_1, stop_2, stop_3, stop_4, stop_5):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    return route


print(add_missing_stops({"from": "New York", "to": "Miami"},
                        stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
                        stop_4="Jacksonville", stop_5="Orlando"))

#{"from": "New York", "to": "Miami", "stops": ["Washington, DC", "Charlotte", "Atlanta", "Jacksonville", "Orlando"]}


# TODO: define the 'extend_route_information()' function
def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    pass


# TODO: define the 'fix_wagon_depot()' function
def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    pass
