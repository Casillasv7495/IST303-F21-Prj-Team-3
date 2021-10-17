   #Need to import services to obtain prices for the services.
    # Guests are charged for every service they reserve. Charges
    # are incurred at the time of reservation.  Reservations are necessary for all services.

    #from django.db import services
    #services.py would include something along the lines of:
    #If these variables already exist in a services.py (That I cannot see...)
    # Replace the equations below with the proper variables

#mineral_bath_a = services.mineral_bath_a
#mineral_bath_b = services.mineral_bath_b

#massage_service_a = services.massage_service_a
#massage_service_b = services.massage_service_b

#facial_service_a = services.facial_service_a
#facial_service_b = services.facial_service_b

#royal_service_a = services.royal_service_a
#royal_service_b = services.royal_service_b


mineral_bath_a = 150.00 #60 min services
mineral_bath_b = 225.00 # 90 min services

massage_service_a = 90.00 #60 min services
massage_service_b = 180.00 #90 min services

facial_service_a = 60.00 #30 min services
facial_service_b = 180.00 #60 min services

royal_service_a = 210.00 #60 min services
royal_service_b = 315.00 #90 min services

total_charge = 0

mineral_bath_q1= input("Mineral bath used? (Yes or No): ")
if mineral_bath_q1.lower() == 'yes': mineral_bath_q2 = input("60 or 90 minute service? (Put '60' or '90')")
if mineral_bath_q2 == '60': total_charge = total_charge + mineral_bath_a
if mineral_bath_q2 == '90': total_charge = total_charge + mineral_bath_b

massage_q1 = input("Were massages given? (Yes or No): ")
if massage_q1.lower() == 'yes': massage_q2 = input("60 or 90 minute service? (Put '60' or '90')")
if massage_q2 == '60': total_charge = total_charge + massage_service_a
if massage_q2 == '90': total_charge = total_charge + massage_service_b

facial_q1 = input("Were facial services given? (Yes or No): ")
if facial_q1.lower() == 'yes': facial_q2 = input("30 or 60 minute service? (Put '30' or '60')")
if facial_q2 == '30': total_charge = total_charge + facial_service_a
if facial_q2 == '60': total_charge = total_charge + facial_service_b

royal_q1 = input("Were royal services given? (Yes or No): ")
if royal_q1.lower() == 'yes': royal_q2 = input("60 or 90 minute service? (Put '60' or '90')")
if royal_q2 == '60': total_charge = total_charge + royal_service_a
if royal_q2 == '90': total_charge = total_charge + royal_service_b

print("******************************************************")
print("The total charge for customer: 'X' is: $" , total_charge)
print("******************************************************")
