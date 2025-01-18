from Product import Product
from Supplier import Supplier

class Suppliers:
    def __init__(self, suppliers=[]):
        self.suppliers = suppliers
    
    def get_by_region(self, region):
        for s in self.suppliers:
            if s.region == region:
                return s
        return None
    
    def seed_data(self):
        seeded_products = [
            Product("Ignition Coil", 3.45, 4),
            Product("Alternator", 7.89, 7),
            Product("Starter Motor", 12.56, 11),
            Product("Timing Belt", 25.34, 15),
            Product("Water Pump", 31.77, 22),
            Product("Brake Pads", 18.92, 19),
            Product("Brake Rotors", 45.23, 9),
            Product("Fuel Filter", 62.89, 12),
            Product("Oil Filter", 27.14, 5),
            Product("Air Filter", 8.76, 3),
            Product("Battery", 39.45, 8),
            Product("Radiator", 53.67, 14),
            Product("Spark Plugs", 22.58, 18),
            Product("Drive Belt", 17.49, 6),
            Product("Clutch Kit", 64.23, 20),
            Product("Transmission Fluid", 5.99, 17),
            Product("Shock Absorbers", 48.12, 21),
            Product("Struts", 36.78, 10),
            Product("Power Steering Pump", 21.84, 13),
            Product("CV Joint", 70.15, 16),
            Product("Wheel Hub", 82.36, 24),
            Product("Differential", 14.72, 25),
            Product("Control Arm", 52.91, 30),
            Product("Ball Joints", 68.47, 27),
            Product("Hub Bearings", 29.53, 32),
            Product("Exhaust Manifold", 12.89, 35),
            Product("Muffler", 74.21, 40),
            Product("Tailpipe", 41.67, 28),
            Product("Headlights", 9.45, 50),
            Product("Taillights", 58.19, 45),
            Product("Side Mirrors", 33.12, 55),
            Product("Window Regulator", 85.47, 60),
            Product("Door Lock Actuator", 19.34, 65),
            Product("Throttle Body", 66.89, 75),
            Product("Mass Air Flow Sensor", 27.99, 85),
            Product("Oxygen Sensor", 79.52, 90),
            Product("Turbocharger", 15.6, 100),
            Product("Fuel Pump", 83.75, 130),
            Product("AC Compressor", 49.36, 160),
            Product("EGR Valve", 26.78, 200)
        ]
        self.suppliers.append(Supplier("Hurstville Mega Store", "Hurstville", "12 Forest Road", [seeded_products[0], seeded_products[18], seeded_products[36], seeded_products[14], seeded_products[32]]))
        self.suppliers.append(Supplier("Rocky Dealership", "Rockdale", "46 Real Street", [seeded_products[1], seeded_products[19], seeded_products[37], seeded_products[15], seeded_products[33]]))
        self.suppliers.append(Supplier("Carlton Spare Parts", "Carlton", "49 Carlton Avenue", [seeded_products[2], seeded_products[20], seeded_products[38], seeded_products[16], seeded_products[34]]))
        self.suppliers.append(Supplier("Big Paulies Warehouse", "Heathcote", "1 Princes Highway", [seeded_products[3], seeded_products[21], seeded_products[39], seeded_products[17], seeded_products[35]]))
        self.suppliers.append(Supplier("Station Street Shop", "Engadine", "13 Station Street", [
        seeded_products[4], seeded_products[22], seeded_products[0], seeded_products[18], seeded_products[36]]))
        self.suppliers.append(Supplier("The Loft(us)", "Loftus", "32A Loftus Avenue", [
        seeded_products[5], seeded_products[23], seeded_products[1], seeded_products[19], seeded_products[37]
    ]))
        self.suppliers.append(Supplier("Sutho Spare Parts", "Sutherland", "14 Existing Street", [
        seeded_products[6], seeded_products[24], seeded_products[2], seeded_products[20], seeded_products[38]
    ]))
        self.suppliers.append(Supplier("Tire City", "Waterfall", "22 Cliff Street", [
        seeded_products[7], seeded_products[25], seeded_products[3], seeded_products[21], seeded_products[39]
    ]))
        self.suppliers.append(Supplier("AutoParts Express", "Mortdale", "66 Wattle Road", [
        seeded_products[8], seeded_products[26], seeded_products[4], seeded_products[22], seeded_products[16]
    ]))
        self.suppliers.append(Supplier("Precision Parts Depot", "Penshurst", "35 Penny Lane", [
        seeded_products[9], seeded_products[27], seeded_products[5], seeded_products[23], seeded_products[17]
    ]))
        self.suppliers.append(Supplier("Car Component Center", "Allawah", "78 Allawah Crescent", [
        seeded_products[10], seeded_products[28], seeded_products[6], seeded_products[24], seeded_products[18]
    ]))
        self.suppliers.append(Supplier("Speedy Spare Solutions", "Kogarah", "20 Forest Road", [
        seeded_products[11], seeded_products[29], seeded_products[7], seeded_products[25], seeded_products[19]
    ]))
        self.suppliers.append(Supplier("Prime Auto Supplies", "Banksia", "102 Banksy Road", [
        seeded_products[12], seeded_products[30], seeded_products[8], seeded_products[26], seeded_products[20]
    ]))
        self.suppliers.append(Supplier("Total Car Parts Hub", "Arncliffe", "77 Arncliffe Place", [
        seeded_products[13], seeded_products[31], seeded_products[9], seeded_products[27], seeded_products[21]
    ]))
        self.suppliers.append(Supplier("DriveLine Parts Warehouse", "Wolli Creek", "99 Princes Highway", [
        seeded_products[14], seeded_products[32], seeded_products[10], seeded_products[28], seeded_products[22]
    ]))
        self.suppliers.append(Supplier("Essential Auto Components", "Sydenham", "44B Metro Way", [
        seeded_products[15], seeded_products[33], seeded_products[11], seeded_products[29], seeded_products[23]
    ]))
        self.suppliers.append(Supplier("Ultimate Parts Source", "Redfern", "56 Rabbitoh Street", [
        seeded_products[16], seeded_products[34], seeded_products[12], seeded_products[30], seeded_products[24]
    ]))
        self.suppliers.append(Supplier("Rapid Repair Parts", "Central", "123 Broadway", [
        seeded_products[17], seeded_products[35], seeded_products[13], seeded_products[31], seeded_products[25]
    ]))
        return self
    
    def __str__(self):
        result = ""
        for s in self.suppliers:
            result += f"\n{s.region}"
        return result