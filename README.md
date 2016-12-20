# python-baytech

Control Baytech devices with Python 3. Currently supports the RPC3-NC PDU via telnet.

## Usage

```python
import baytech.rpc3nc as rpc3nc

HOST = "192.168.0.10"
command_prompt = b'>'
timeout = 60

tn = rpc3nc.RPC3_NC(HOST, timeout= timeout, command_prompt= command_prompt)
tn.connect()
tn.turnOn(4)
status = tn.getStatus()
tn.close()

print 'Baytech: %s' % (status)
```

## Contributions

Pull requests are welcome. Possible areas for improvement:

* Additional Baytech devices.

## Disclaimer

Not affiliated with Bay Technical Associates,
