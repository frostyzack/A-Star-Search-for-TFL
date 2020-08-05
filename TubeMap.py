#This file defines the Station class and constructs the Tube map (adjacency list) of station objects as the nodes
class Station:
    def __init__(self, name, ics_code, zone, total_lines, latitude, longitude):
        self._name = name
        self._ics_code = ics_code  # Used to get API Live Data
        self._zone = zone
        self._total_lines = total_lines
        self._latitude = latitude
        self._longitude = longitude

    # Getters
    def getName(self):
        return self._name

    def getIcsCode(self):
        return self._ics_code

    def getZone(self):
        return self._zone

    def getTotalLines(self):
        return self._total_lines

    def getLatitude(self):
        return self._latitude

    def getLongitude(self):
        return self._longitude

acton_town = Station('Acton Town', 1000002, 3, 2, 51.5028, -0.2801)
aldgate = Station('Aldgate', 1000003, 1, 2, 51.5143, -0.0755)
aldgate_east = Station('Aldgate East', 1000004, 1, 2, 51.5154, -0.0726)
all_saints = Station('All Saint\'s', 1002003, 2, 1, 51.5107, -0.013)
alperton = Station('Alperton', 10000052, 4, 1, 51.5407, -0.2997)
angel = Station('Angel', 1000007, 1, 1, 51.5322, -0.1058)
archway = Station('Archway', 1000008, 2.5, 1, 51.5653, -0.1353)
arnos_grove = Station('Arnos Grove', 1000009, 4, 1, 51.6164, -0.1331)
arsenal = Station('Arsenal', 1000010, 2, 1, 51.5586, -0.1059)
baker_street = Station('Baker Street', 1000011, 1, 5, 51.5226, -0.1571)
balham = Station('Balham', 1000012, 2, 1, 51.4431, -0.1525)
bank = Station('Bank', 1000013, 1, 4, 51.5133, -0.0886)
barbican = Station('Barbican', 1000014, 1, 3, 51.5204, -0.0979)
barking = Station('Barking', 1000015, 4, 2, 51.5396, 0.081)
barkingside = Station('Barkingside', 1000016, 5, 1, 51.5856, 0.0887)
barons_court = Station('Barons Court', 1000017, 2, 2, 51.4905, -0.2139)
bayswater = Station('Bayswater', 1000018, 1, 2, 51.5121, -0.1879)
beckton = Station('Beckton', 1002011, 3, 1, 51.5148, 0.0613)
beckton_park = Station('Beckton Park', 1002012, 3, 1, 51.5087, 0.055)
becontree = Station('Becontree', 1000019, 5, 1, 51.5403, 0.127)
belsize_park = Station('Belsize Park', 1000020, 2, 1, 51.5504, -0.1642)
bethnal_green = Station('Bethnal Green', 1000022, 2, 1, 51.527, -0.0549)
blackfriars = Station('Blackfriars', 1000023, 1, 2, 51.512, -0.1031)
blackhorse_road = Station('Blackhorse Road', 1000024, 3, 1, 51.5867, -0.0417)
blackwall = Station('Blackwall', 1002018, 2, 1, 51.5079, -0.0066)
bond_street = Station('Bond Street', 1002018, 2, 1, 51.5079, -0.0066)
borough = Station('Borough', 1000026, 1, 1, 51.5011, -0.0943)
boston_manor = Station('Boston Manor', 1000027, 4, 1, 51.5011, -0.0943)

# Sample used for testing algorithm
edgeware_road = Station('Edgware Road', 1000072, 1, 3, 51.5203, -0.17)
notting_hill_gate = Station('Notting Hill Gate', 1000167, 1.5, 3, 51.5094, -0.1967)
high_street_kensington = Station('High Street Kensington', 1000110, 1, 2, 51.5009, -0.1925)
gloucester_road = Station('Gloucester Road', 1000086, 1, 3, 51.4945, -0.1829)
south_kensington = Station('South Kensington', 1000212, 1, 3, 51.4941, -0.1738)
sloane_square = Station('Sloane Square', 1000206, 1, 2, 51.4924, -0.1565)
victoria = Station('Victoria', 1000206, 1, 2, 51.4965, -0.1447)
st_james_park = Station('St. James\'s Park', 1000221, 1, 2, 51.4994, -0.1335)
westminster = Station('Westminster', 1000266, 1, 3, 51.501, -0.1254)
# Adjacency List of Station Nodes

Tube_map = {
    edgeware_road: {bayswater},
    bayswater: {edgeware_road, notting_hill_gate},
    notting_hill_gate: {bayswater, high_street_kensington},
    high_street_kensington: {notting_hill_gate, gloucester_road},
    gloucester_road: {high_street_kensington, south_kensington},
    south_kensington: {gloucester_road, sloane_square},
    sloane_square: {south_kensington, victoria},
    victoria: {sloane_square, st_james_park},
    st_james_park: {victoria, westminster}
}