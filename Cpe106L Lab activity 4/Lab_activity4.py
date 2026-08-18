import unittest

class Order:
    def __init__(self, orderID, delivered=False):
        self.orderID = orderID
        self.delivered = delivered

    def orderStatus(self):
        if self.delivered == False:
            return "Not yet delivered/Pending"
        else:
            return "Delivered"
       

class Transit:
    instance = None
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Transit, cls).__new__(cls)
            cls.instance.orders = []
        return cls.instance

    def add_item(self, order:Order):
        self.orders.append(order)
        print(f"\nOrder Added")

    def display_Inventory(self):
        print("\nCurrent Orders in the system:")
        if len(self.orders) == 0:
            print("No order placed")
        else: 
            for order in self.orders:
                print(f"\norderID: [{order.orderID}] | Status: [{order.orderStatus()}]")


    def Delivered_order(self,Search_ID):  
        if len(self.orders) == 0:
            print("No order name")
        else:      
            for order in self.orders:
                if Search_ID == order.orderID:
                    print("ID found in system")
                    print(f"\nCurrent info: orderID: [{order.orderID}] | Status: [{order.orderStatus()}]\n")
                    order.delivered = True
                    print("Updating...............")
                    print(f"Updated info: orderID: [{order.orderID}] | Status: [{order.orderStatus()}]\n")
                    print("-Status Updated-")
                    return True
                
            print("\nOrder does not exist in system")
            return False

class TestingTransitSystem(unittest.TestCase):
    def setUp(self):
        transit = Transit()
        transit.orders.clear()
    
    def testing1_adding_order(self):
        print("\nTest: Adding order")
        transit = Transit()
        print("\nEntering order....")
        order = Order("TestCode - 001", delivered = False)
        transit.add_item(order)
        print("\nDisplaying orders....")
        transit.display_Inventory()
        self.assertEqual(order.orderStatus(), "Not yet delivered/Pending")
        self.assertFalse(order.delivered)
        print("____________________________________________________________________")
        
    
    def testing2_DeliveredOrder(self):
        print("\nTest: Upating order to [Delivered]")
        transit = Transit()
        print("\nEntering order....")
        order = Order("TestCode - 002", delivered = False)
        transit.add_item(order)
        print("\nDisplaying orders....")
        transit.display_Inventory()
        success = transit.Delivered_order("TestCode - 002")
        print("\nDisplaying orders....")
        transit.display_Inventory()
        self.assertTrue(success)
        self.assertTrue(order.delivered)
        self.assertEqual(order.orderStatus(), "Delivered")
        print("____________________________________________________________________")

    def testing3_invalid_order(self):
        print("\nTest: Displaying Invalid messaged when wrong or nonexisting ID was entered (With existing errors in the system)")
        transit = Transit()
        print("\nEntering order....")
        order = Order("RANDOM-ID", delivered = False)
        transit.add_item(order)
        print("\nDisplaying orders....")
        transit.display_Inventory()
        print("\nEntering Wrong order....")
        success = transit.Delivered_order("WRONG-ID")
        self.assertFalse(success)
        print("____________________________________________________________________")

    def testing4_Empty_list(self):
        print("\nTest: Displaying Empty List or No order Message")
        print("\nDisplaying orders....")
        transit = Transit()
        success = transit.display_Inventory()
        self.assertFalse(success)
        print("____________________________________________________________________")


    
if __name__ == "__main__":
    unittest.main()