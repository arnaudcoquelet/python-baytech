# python-baytech

Control Baytech devices with Python 3. Currently supports the RPC3-NC PDU via telnet.

## Usage

```python
from baytech.rpc3-nc import RPC3_NC

hosts = discover() # Discover devices on your local network.
s20 = S20("x.x.x.x") # Use a discovered host, or supply a known host.
print(s20.on) # Current state (True = ON, False = OFF).
s20.on = True # Turn it on.
s20.on = False # Turn it off.
```

## Contributions

Pull requests are welcome. Possible areas for improvement:

* Additional Baytech devices.

## Disclaimer

Not affiliated with Bay Technical Associates,
