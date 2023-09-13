# This is the comment

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
        next_node_pointer = next((key for key in sorted(self.DHT.keys()) if key > node), None)
        if next_node_pointer is None:
            next_node_pointer = min(self.DHT.keys())
        return next_node_pointer
    
    def find_predecessor(self, node):
        self.DHT.keys().sort()
        maxm = max(self.DHT.keys())
        minm = min(self.DHT.keys())
        if node == minm:
            predecessor_node = maxm
        else:
            predecessor_node = self.DHT.keys()[node - 1]
        return predecessor_node

    def is_file_present(self, left, key, right):
        if left == right:
            return True 
        if left < right:
            return left < key <= right
        return (left < key <= self.space - 1) or (0 <= key <= right)
    
    def get_dht_size(self):
        return len(self.DHT)

    def print_nodes(self):
        if not self.DHT:
            print("No Nodes in the network!")
            return
        print("{", end = "")
        for node in self.DHT:
            print(node, ",", end = " ")
        print("}")

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

    def leave(self, node):
        if node not in self.DHT:
            print(f"Node {node} does not exist.")
            return

        del self.DHT[node]
        self.update_all_finger_tables()

    def print_finger_tables(self):
        if not self.DHT:
            print("Network is empty!")
            return 
        
        print("\t i   id + 2^i   successor")
        for node, finger_table in self.DHT.items():
            print(f"Node {node} ->")
            for i, (key, successor) in enumerate(finger_table):
                print(f"\t{i}\t{key}\t{successor}")

    def search(self, file_index, start_node):
        if start_node not in self.DHT:
            print("Start node does not exist.")
            return -1
        
        max_ = -1
        for key in self.DHT.keys():
            if key < start_node:
                max_ = key
            else:
                max_ = -1
        predecessor_node = max_
        if predecessor_node == -1:
            predecessor_node = max(self.DHT.keys())
        if self.is_file_present(predecessor_node, file_index, start_node):
            print(start_node)
            return start_node
        
        min_ = self.space + 1
        for key in self.DHT.keys():
            if key > start_node:
                min_ = key
            else:
                min_ = self.space + 1
        successor_node = min_
        if successor_node is self.space + 1:
            successor_node = min(self.DHT.keys())
        if self.is_file_present(start_node, file_index, successor_node):
            print(f"{start_node} -> ", end = "")
            return successor_node
        
        finger_table = self.DHT[start_node]
        for i in range(self.m - 1, -1, -1):
            if self.is_file_present(start_node, finger_table[i][i], file_index):
                print(f"{start_node} -> ", end = "")
                return self.search(file_index, finger_table[i][1])
            
        return -1
    
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
            file_id = int(input("Enter Node ID to search for: "))
            node_id = int(input("Enter Node ID to begin search from: "))
            print("Search Path: ", end = "")
            N.search(file_id, node_id)
        elif choice == 4:
            N.print_finger_tables()
        elif choice == 5:
            break
        else:
            print("Invalid Choice.")

        print()
        print("----------------------------------------------------------------")
        print()

def main():
    m = int(input("Number of Bits to be allocated for search space(m): "))
    input_network(createChordNetwork(m))

if __name__ == "__main__":
    main()