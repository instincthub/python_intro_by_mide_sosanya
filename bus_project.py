###############logic and data############
#buses object attributes
class Bus:
    stops = []
    def __init__(self, final_destination, bus_id, final_dest_price, midway_price, stops, canStopMidway):
        self.bus_id = bus_id
        self.final_destination = final_destination
        self.final_dest_price = final_dest_price
        self.midway_price = midway_price
        self.stops = stops
        self.canStopMidway = canStopMidway
buses = [ Bus(final_destination="CMS", bus_id="771", final_dest_price=400, midway_price=300, stops=[], canStopMidway=False), \
    Bus(final_destination="OBALENDE", bus_id="772", final_dest_price=300, midway_price=250, stops=["Adeniyi"], canStopMidway=True), \
    Bus(final_destination="Oshodi", bus_id="773", final_dest_price=500, midway_price=400, stops=["Mile 2"], canStopMidway=True)]
#rides
class Ride:
    def __init__(self, bus, final_dest):
        self.bus =bus
        self.final_dest = final_dest
#virtual bus cards
class VirtualCard:
    avail_bal = 200
    def __init__(self, card_id, pin):
        self.card_id = card_id
        self.pin = pin
    def can_pay(self, ride):
        print("Your card balance is " + str(self.avail_bal))
        if ride.final_dest:
            if self.avail_bal >= ride.bus.final_dest_price:
                return True
            else:
                return False
        else:
            if self.avail_bal >= ride.bus.midway_price:
                return True
            else:
                return False
    def pay_for_ride(self, ride):
        if ride.final_dest:
            self.avail_bal = self.avail_bal - ride.bus.final_dest_price
        else:
            self.avail_bal = self.avail_bal - ride.bus.midway_price


cards = [VirtualCard(card_id="77851", pin="8522"),\
         VirtualCard(card_id="77852", pin="3345"),\
         VirtualCard(card_id="77853", pin="0986"),]
#print("Going to new line \t gone!")


############user interface#############
print("Here is a list of availbale buses:")
counter = 1
for bus in buses:
    print("("+str(counter)+") " + "Bus ID: " + bus.bus_id)
    print("\tFinal Destination: " + bus.final_destination)
    print("\t Can Stop Midway: " + str(bus.canStopMidway))
    print("\tStops: " + str(bus.stops))
    print("\tFinal Destination Price: " + str(bus.final_dest_price))
    print("\tMid Way Price: " + str(bus.midway_price))
    counter += 1
user_preferred_bus = input("Please enter the bus id of your preferred bus: \n >>>>")
preferred_bus  = None
for bus in buses:
    if user_preferred_bus == bus.bus_id:
        preferred_bus  = bus
    else:
        continue
if preferred_bus is None:
    print("You selected an invalid bus")
else:
    print("Your bus is going to " + preferred_bus.final_destination)
    is_going_to_final = input("Are you stopping at the last bus stop? Y/N \n")
    if is_going_to_final == "Y":
        ride = Ride(bus=preferred_bus, final_dest=True)
    else:
        ride = Ride(bus=preferred_bus, final_dest=False)
    user_card = None
    collect_card_id = input("Please, enter your card ID: \n")
    for card in cards:
        if card.card_id == collect_card_id:
            user_card  = card
        else:
            continue
    if user_card is None:
        print("Error: No matching Card ID was found")
    else:
        collect_pin = input("Please enter your 4-digit pin: \n")
        if user_card.pin == collect_pin:
            print("Correct Pin!")
            if user_card.can_pay(ride):
                print("Charge Card!")
                user_card.pay_for_ride(ride)
                print("Successful, Enjoy your trip!")
                print("Your new balance is " + str(user_card.avail_bal))
            else:
                print("Oops, insuficient balance!")
        else:
            print("Error: Wrong Pin!")


        
