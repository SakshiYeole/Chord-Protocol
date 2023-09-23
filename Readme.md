# Network Systems and Security

---

## Implementation of Chord Protocol
## Following are my details for assignment submission:
<p>Name: &nbsp;&nbsp;&nbsp;&nbsp;Sakshi Shashikant Yeole</p>
<p>Roll No.: &nbsp;20CS01047</p>
<p>Semester: &nbsp;7th</p>
<p>Year of study: &nbsp;4th year</p>
<p>Assignment: &nbsp;Assignment - 1</p>

---

## Run Locally
1. Clone the repository: https://github.com/SakshiYeole/Chord-Protocol.git
2. Open in your favourite editor. (The editor used while making this project is VS Code and also the path are currently coded to handle only windows)
3. Run the complete project by running the chordProtocol.py. Follow the prompt to give input.

## Problem Statement
Implement Chord routing protocol for P2P Networks. Your implementation must include Key Look up, Node-join/leave with stabilization. Analyze the complexity of your implementation. Write a report on security issues of Chord protocol.

<details>
<summary>Details:</summary>

<p>Give input the number of bits for the Chord Network</p>

</details>

## Understanding the codebase
<p>The file consists of many functions, lets walk through one after another.</p>

1. ***update_all_finger_tables***:
   
   <p>This method updates the finger tables for all nodes in the network. It iterates through all nodes ('n' iterations), and for each node, it updates 'm' finger table entries by calling *self.find_successor*.</p>

2. ***find_successor***:
   
   <p>This method finds the successor of a given node. It performs a binary search on the sorted keys of the DHT dictionary to find the successor.</p>

3. ***find_predecessor***:
   <p>This method finds the predecessor of a given node. It also performs a binary search on the sorted keys of the DHT dictionary.</p>

4. ***get_dht_size, print_nodes, join, leave, print_finger_tables***:
   <p>These methods involve simple operations on the DHT or printing nodes and finger tables.</p>

5. ***find_closest_preceding_node, find_closest_succeeding_node, is_key_present, search***:
    <p>These methods are used for searching in the Chord network and have time complexity proportional to the number of nodes in the network and the number of bits (m)</p>

6. ***input_network*** (user interaction function):
    <p>This function allows the user to interact with the Chord network, performing operations like joining, leaving, searching, and displaying finger tables. The time complexity of Chord network operations depends on the operation type and Chord method called.</p>

7. ***main***:
    <p>The main function initializes the Chord network based on user input for the number of bits (m) and then calls input_network for user interaction.</p>


## Work Flow of the code

1. Create empty output directory.
2. Run the chordProtocol.py file and give the input for number of bits in chord network to create.
3. Give in the choice nummber according to choices printed on the console.
4. The program will work according to user's choice and corresponding inputs provided.
5. Finally close the program after you are done processing.

<p>For more details regarding Complexity Analysis and the Security Issues regarding the chord protocol, check the docx file: <a href="https://github.com/SakshiYeole/Chord-Protocol/blob/main/Security%20Issues.docx">"Security Issues.docx"</a></p>