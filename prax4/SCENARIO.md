## Base Scenario

- There is a node on port 5000 (master)
- We add a node on port 5001
- The client knows about the node 5000, asks for a list of nodes
- The client sends a message 5000, 5001, they respond
- We take down the node 50001
- The client sends a message 5000, 5001. 5001 does not respond. It is removed from the list


http://localhost:5001

POST http://localhost:5001/inv {data}