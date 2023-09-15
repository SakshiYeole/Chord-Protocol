class createChordNetwork:
    # create a network with m as no of bits
    def __init__(self, m) -> None:
        self.m = m
        self.space = 2 ** m
        self.DHT = {}

    # Update is same as creating finger table when not createdd
    def update_all_finger_tables(self):
        for node, finger_table in self.DHT.items():
            for i in range(len(finger_table)):
                finger_table[i] = (finger_table[i][0], self.find_successor(finger_table[i][0]))
                self.DHT[node] = finger_table

    # successor is the next node in network
    def find_successor(self, node):
        sorted_keys = sorted(self.DHT.keys())
        
        next_node_pointer = None
        for key in sorted_keys:
            if key > node:
                next_node_pointer = key
                break

        if next_node_pointer is None:
            next_node_pointer = min(sorted_keys)
        return next_node_pointer
    
    # Tested
    def find_predecessor(self, node):               
        sorted_keys = sorted(self.DHT.keys())
        # sorted_keys = sorted(keys)
        maxm = max(sorted_keys)
        minm = min(sorted_keys)
        if node == minm:
            predecessor_node = maxm
        else:
            index = sorted_keys.index(node)
            predecessor_node = sorted_keys[index - 1]
        return predecessor_node

    # Tested
    def get_dht_size(self):
        return len(self.DHT)

    # Tested
    def print_nodes(self):
        if not self.DHT:
            print("No Nodes in the network!")
            return
        print("{", end = "")
        for node in self.DHT:
            print(node, ",", end = " ")
        print("}")

    # Tested
    def join(self, node):
        if node < 0 or node >= self.space:
            print(f"Invalid Node ID. (Node ID must be in the range[0, {self.space - 1}])")
            return
        if node in self.DHT:
            print(f"Node {node} is already present in the network")
            return
        
        finger_table = [(0, 0) for _ in range(self.m)]
        for i in range(self.m):
            temp = 2 ** i
            finger_table[i] = ((node + temp) % self.space, 0)

        self.DHT[node] = finger_table
        self.update_all_finger_tables()

    # Tested
    def leave(self, node):
        if node not in self.DHT:
            print(f"Node {node} does not exist.")
            return

        del self.DHT[node]
        self.update_all_finger_tables()

    # Tested
    def print_finger_tables(self):
        if not self.DHT:
            print("Network is empty!")
            return 
        
        print("\t i   id + 2^i   successor")
        for node, finger_table in self.DHT.items():
            print(f"Node {node} ->")
            for i, (key, successor) in enumerate(finger_table):
                print(f"\t{i}\t{key}\t{successor}")

    # Tested
    def find_closest_preceding_node(self, keyID, keys):
        # keys = list(self.DHT.keys())
        keys.sort()
        if keyID < min(keys):
            return max(keys)
        elif keyID > max(keys):
            return max(keys)
        else:
            for i in range(len(keys)):
                if keys[i] < keyID < keys[i+1]:
                    return keys[i]
        return -1

    #Tested
    def find_closest_succeeding_node(self, keyID):
        keys = list(self.DHT.keys())
        keys.sort()
        if keyID < min(keys):
            return min(keys)
        elif keyID > max(keys):
            return min(keys)
        else:
            for i in range(len(keys)):
                if keys[i] < keyID < keys[i+1]:
                    return keys[i+1]
        return -1
    
    # Tested
    def is_key_present(self, left, key, right):
        if left == right:
            return key == left
        if left < right:
            return left < key <= right
        return (left < key <= self.space - 1) or (0 <= key <= right)
    
    def search(self, keyID, start_node):
        keyID = hash(keyID)
        if start_node not in self.DHT:
            print("Start node does not exist.")
            return -1

        # predecessor_node = self.find_predecessor(start_node)
        successor_node = self.find_successor(start_node)
        if self.is_key_present(start_node , keyID, successor_node):
            print(f"{start_node} -> {successor_node}", end = "")
            return successor_node
        else:
            destination_node = self.find_closest_succeeding_node(keyID)
            if start_node == destination_node:
                print(f"{start_node}", end = "")
                return
            else:
                finger_table = self.DHT[start_node]
                keys = []
                for i, (entry, successor) in enumerate(finger_table):
                    keys.append(successor)
                    print(f"{start_node} -> ", end = "")
                    return self.search(keyID, self.find_closest_preceding_node(keyID, keys))

# Tested
def input_network(N):
    while(True):
        print()
        print(f"Number of Nodes in the network: {N.get_dht_size()}")
        print("Nodes in the network: ", end = "")
        N.print_nodes()
        print(" 1. Join Network\n 2. Leave Network\n 3. Search File\n 4. Show Finger Tables\n 5. Close")
        choice = int(input("Enter Choice: "))

        if choice == 1:
            node_id = int(input("Enter Node ID: "))
            N.join(node_id)
        elif choice == 2:
            node_id = int(input("Enter Node ID: "))
            N.leave(node_id)
        elif choice == 3:
            key_id = int(input("Enter Node ID to search for: "))
            node_id = int(input("Enter Node ID to begin search from: "))
            print("Search Path: ", end = "")
            N.search(key_id, node_id)
        elif choice == 4:
            N.print_finger_tables()
        elif choice == 5:
            break
        else:
            print("Invalid Choice.")

        print()
        print("----------------------------------------------------------------")
        # print()

def main():
    m = int(input("Number of Bits to be allocated for search space (m): "))
    input_network(createChordNetwork(m))

    # Testing
    # t= createChordNetwork(3)
    # keys = [1, 3, 5]
    # print(t.find_predecessor(5, keys))
    # print(t.find_successor(4, keys))
    # print(t.get_dht_size())
    # print(t.is_key_present(5, 7, 3))
    # print(t.find_closest_preceding_node(6, keys))
    # print(t.find_closest_succeeding_node(0, keys))

if __name__ == "__main__":
    main()