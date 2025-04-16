# ITI0215_25

Code examples for the practice sessions of course "ITI0215 Distributed Systems"

* `prax1` we started building a server based on Python `http.server`.
* `prax2` we continued implementing `http.server` based server, including:
    - using `nodemon` for mode streamlined development process: `nodemon ./server.py 5000`
    - implemented `POST` request handling in server.
    - `client.py` for automating making requests via `requests` library.
* `prax3` started to construct P2P network:
    - extended `http.server`-based implemnentation to be multi threaded
    - application architecture improvements; configuration management.
    - started to implement topology and scenario as describred in `SCENARIO.md` 
* `prax4` implemented a basic network. We still need to refactor the code so that 
    a. the network recovers in case of nodes going offline
    b. information about network topology is stored in single location
* `prax5` moved configuration and node management to separate module for cleaner code and logic
* `prax6` - Addded custom logger for better demo/understandability. See `node.py` for usage example
* Gradings took place during weeks 7 and 8


## API Calls

- `/addr?port=<port>`: Ask for a list of nodes from master. If `port` is provided then the master adds it to the list of known nodes if it does not exist there.  

