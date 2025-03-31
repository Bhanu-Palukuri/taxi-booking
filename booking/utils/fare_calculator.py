def calculate_fare(distance_km, base_fare=5, per_km_rate=2):
    """
    Calculate taxi fare based on distance.

    :param distance_km: Distance traveled in km.
    :param base_fare: Fixed starting fare (default $5).
    :param per_km_rate: Charge per km (default $2).
    :return: Total fare.
    """
    if distance_km < 0:
        raise ValueError("Distance cannot be negative.")

    total_fare = base_fare + (distance_km * per_km_rate)
    return round(total_fare, 2)
  
