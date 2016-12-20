import sys
sys.path.append('../')
import baytech.rpc3nc as rpc3nc


if __name__ == '__main__':
    HOST = "10.17.19.249"
    command_prompt = b'>'
    timeout = 60

    tn = rpc3nc.RPC3_NC(HOST, timeout= timeout, command_prompt= command_prompt)
    tn.connect()
    tn.turnOn(4)
    status = tn.getStatus()
    tn.close()


    print 'Baytech: %s' % (status)
