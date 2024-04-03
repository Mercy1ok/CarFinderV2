AllowedVehiclesList = [
    'Ford F-150',
    'Chevrolet Silverado',
    'Tesla CyberTruck',
    'Toyota Tundra',
    'Nissan Titan'
] 

Authorized_Cars = AllowedVehiclesList[0] + ', ' + AllowedVehiclesList[1] + ', ' + AllowedVehiclesList[3] + ', ' + AllowedVehiclesList[4]

UnAuthorized_Cars = AllowedVehiclesList[2]

menu = """********************************
AutoCountry Vehicle Finder v0.2
********************************
Please Enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. SEARCH for all Authorized Vehicle
3. Exit"""

print(menu)

option = int(input("Enter your choice: "))

if option == 1:
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for vehicle in AllowedVehiclesList:
        print(                                            )
        print(vehicle)
    print(                                              )
    print(menu) 
  
elif option == 2:
  print('*******************************')
  selected_car = "Please Enter the full Vehicle name: "
  selected_caro = input(f"\033[1m{selected_car}\033[0m")
 

  if selected_caro in Authorized_Cars:
      print('                                      ')
      selecteddd = f"{selected_caro} is an authorized vehicle."
      print(f"\033[1m{selecteddd}\033[0m")
      print(menu)
  elif selected_caro in UnAuthorized_Cars:
      print('                                      ')
      unselected = f"{selected_caro} is not an authorized vehicle, if you received this in error please check the spelling and try again."
      print(f"\033[1m{unselected}\033[0m")
      print(menu)
  else:
      print("Invalid car selection.")

elif option == 3:
    print("Thank you for using the AutoCountry Vehicle Finder, goodbye!")

else:
    print("Invalid option")
