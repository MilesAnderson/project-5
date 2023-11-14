"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    openTime = arrow.get(brevet_start_time)  
    time = 0

    if control_dist_km > (brevet_dist_km + (brevet_dist_km*.20)):
        cont = brevet_dist_km//1
    elif control_dist_km > brevet_dist_km and control_dist_km <= (brevet_dist_km + (brevet_dist_km*.20)):
        cont = brevet_dist_km//1
    else:
        cont = control_dist_km//1

    if cont > 600 and cont <=1000:
        time+=(cont-600)/28
        cont = 600
    if cont > 400 and cont <=600:
        time+=(cont-400)/30
        cont = 400
    if cont > 200 and cont <=400:
        time+=(cont-200)/32
        cont = 200
    if cont > 0 and cont <=200:
        time+=cont/34

    hour = time//1
    minute = round((time-hour)*60)

    return openTime.shift(hours=+hour, minutes=+minute)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    closeTime = arrow.get(brevet_start_time)
    time = 0

    if control_dist_km > (brevet_dist_km + (brevet_dist_km*.20)):
        cont = brevet_dist_km//1
    elif control_dist_km > brevet_dist_km and control_dist_km <= (brevet_dist_km + (brevet_dist_km*.20)):
        cont = brevet_dist_km//1
    else:
        cont = control_dist_km//1

    if cont > 600 and cont <= 1000:
        time+=(cont-600)/11.428
        cont = 600
    if cont > 60 and cont <= 600:
        time+=cont/15
    if cont > 0 and cont <=60:
        time+=(cont/20)+1
    if cont == 0:
        time = 1

    hour = time//1
    minute = round((time-hour)*60)

    if cont == 200 and brevet_dist_km == 200:
        minute+=10
    if cont == 400 and brevet_dist_km == 400:
        minute+=20

    return closeTime.shift(hours=+hour, minutes=+minute)
