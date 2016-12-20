import telnetlib
import re
import logging


_LOGGER = logging.getLogger(__name__)

RE_AveragePower = r'(Average Power):\s*(\d+\s*Watts)'
RE_TrueRmsVoltage = r'(True RMS Voltage):\s*(\d+.*\d*\s*Volts)'
RE_TrueRmsCurrent = r'(True RMS Current):\s*(\d+.*\d*\s*Amps)'
RE_MaximumDetected = r'(Maximum Detected):\s*(\d+.*\d*\s*Amps)'
RE_CircuitBreaker = r'(Circuit Breaker):\s*(\w+)'
RE_InternalTemperature = r'(Internal Temperature):\s*(\d+.*\d*\s*C)'

RE_Outlet1 = r'1\)\.*\b(.*)\b\s*:\s*(\w*)'
RE_Outlet2 = r'2\)\.*\b(.*)\b\s*:\s*(\w*)'
RE_Outlet3 = r'3\)\.*\b(.*)\b\s*:\s*(\w*)'
RE_Outlet4 = r'4\)\.*\b(.*)\b\s*:\s*(\w*)'
RE_Outlet5 = r'5\)\.*\b(.*)\b\s*:\s*(\w*)'
RE_Outlet6 = r'6\)\.*\b(.*)\b\s*:\s*(\w*)'
RE_Outlet7 = r'7\)\.*\b(.*)\b\s*:\s*(\w*)'
RE_Outlet8 = r'8\)\.*\b(.*)\b\s*:\s*(\w*)'


class RPC3_NC(object):
    """ Controls an BayTech ROC3-NC PDU.
    """
    def __init__(self, host, port=23, timeout=10, command_prompt=b'>'):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.command_prompt = command_prompt
        self.telnet = None
        self.connected = False

    def connect(self):
        self.telnet = telnetlib.Telnet(self.host, port= self.port, timeout = self.timeout)
        prompt = self.telnet.read_until(self.command_prompt, self.timeout)

        if self.command_prompt in prompt:
            self.connected = True
            return True, None
        else:
            return False, 'Cannot connect to %s:%s' % (self.host, self.port)

    def close(self):
        if self.telnet is not None and self.connected:
            self.telnet.write(b'exit\r\n')
            self.telnet.close()

    def _parseStatus(self, raw_status):
        status = {}

        if raw_status is None:
            return status

        raw_status = raw_status.decode("utf-8")

        _LOGGER.debug('Raw Status:\n%s' % ( raw_status ) )

        #AveragePower
        m= re.findall(RE_AveragePower, raw_status)
        if m and len(m) >=1:
            _LOGGER.debug( '%s' % (m) )
            key,value = m[0]
            status[key] = value
        else:
            _LOGGER.debug( 'No match' )


        #RE_TrueRmsVoltage
        m = re.findall(RE_TrueRmsVoltage,raw_status)
        if m and len(m) >=1:
            _LOGGER.debug( '%s' % (m) )
            key,value = m[0]
            status[key] = value
        else:
            _LOGGER.debug( 'No match' )

        #RE_TrueRmsCurrent
        m = re.findall(RE_TrueRmsCurrent,raw_status)
        if m and len(m) >=1:
            _LOGGER.debug( '%s' % (m) )
            key,value = m[0]
            status[key] = value
        else:
            _LOGGER.debug( 'No match' )

        #RE_MaximumDetected
        m = re.findall(RE_MaximumDetected,raw_status)
        if m and len(m) >=1:
            _LOGGER.debug( '%s' % (m) )
            key,value = m[0]
            status[key] = value
        else:
            _LOGGER.debug( 'No match' )

        #RE_CircuitBreaker
        m = re.findall(RE_CircuitBreaker,raw_status)
        if m and len(m) >=1:
            _LOGGER.debug( '%s' % (m) )
            key,value = m[0]
            status[key] = value
        else:
            _LOGGER.debug( 'No match' )

        #RE_InternalTemperature
        m = re.findall(RE_InternalTemperature,raw_status)
        if m and len(m) >=1:
            _LOGGER.debug( '%s' % (m) )
            key,value = m[0]
            status[key] = value
        else:
            _LOGGER.debug( 'No match' )

        outlets = {}

        #RE_Outlet1
        m = re.findall(RE_Outlet1,raw_status)
        if m and len(m) >=1:
            _LOGGER.debug( '%s' % (m) )
            key,value = m[0]
            if key=='':
                key = 'Outlet 1'
            outlets['1'] = {key: value}
        else:
            outlets['1'] = {}
            _LOGGER.debug( 'No match' )

        #RE_Outlet2
        m = re.findall(RE_Outlet2,raw_status)
        if m and len(m) >=1:
            _LOGGER.debug( '%s' % (m) )
            key,value = m[0]
            if key=='':
                key = 'Outlet 2'
            outlets['2'] = {key: value}
        else:
            outlets['2'] = {}
            _LOGGER.debug( 'No match' )

        #RE_Outlet3
        m = re.findall(RE_Outlet3,raw_status)
        if m and len(m) >=1:
            _LOGGER.debug( '%s' % (m) )
            key,value = m[0]
            if key=='':
                key = 'Outlet 3'
            outlets['3'] = {key: value}
        else:
            outlets['3'] = {}
            _LOGGER.debug( 'No match' )

        #RE_Outlet4
        m = re.findall(RE_Outlet4,raw_status)
        if m and len(m) >=1:
            _LOGGER.debug( '%s' % (m) )
            key,value = m[0]
            if key=='':
                key = 'Outlet 4'
            outlets['4'] = {key: value}
        else:
            outlets['4'] = {}
            _LOGGER.debug( 'No match' )

        #RE_Outlet5
        m = re.findall(RE_Outlet5,raw_status)
        if m and len(m) >=1:
            _LOGGER.debug( '%s' % (m) )
            key,value = m[0]
            if key=='':
                key = 'Outlet 5'
            outlets['5'] = {key: value}
        else:
            outlets['5'] = {}
            _LOGGER.debug( 'No match' )

        #RE_Outlet6
        m = re.findall(RE_Outlet6,raw_status)
        if m and len(m) >=1:
            _LOGGER.debug( '%s' % (m) )
            key,value = m[0]
            if key=='':
                key = 'Outlet 6'
            outlets['6'] = {key: value}
        else:
            outlets['6'] = {}
            _LOGGER.debug( 'No match' )
        status['outlets'] = outlets

        #RE_Outlet7
        m = re.findall(RE_Outlet7,raw_status)
        if m and len(m) >=1:
            _LOGGER.debug( '%s' % (m) )
            key,value = m[0]
            if key=='':
                key = 'Outlet 7'
            outlets['7'] = {key: value}
        else:
            outlets['7'] = {}
            _LOGGER.debug( 'No match' )

        #RE_Outlet8
        m = re.findall(RE_Outlet8,raw_status)
        if m and len(m) >=1:
            _LOGGER.debug( '%s' % (m) )
            key,value = m[0]
            if key=='':
                key = 'Outlet 8'
            outlets['8'] = {key: value}
        else:
            outlets['8'] = {}
            p_LOGGER.debug( 'No match' )

        status['outlets'] = outlets
        return status


    def getStatus(self, outlet=-1):
        if self.telnet is not None and self.connected:
            self.telnet.write(b'status\r\n')
            response = self.telnet.read_until(self.command_prompt, self.timeout)

            status = self._parseStatus(response)

            if outlet < 1:
                #Return All
                return status
            elif outlet <=8:
                key = '%s' % (outlet)
                return status['outlets'][key]
            else :
                return {}

        else:
            return {}

    def turnOn(self, outlet=-1):
        if self.telnet is not None and self.connected:
            if outlet >=1 and outlet <=8:
                self.telnet.write(b'On %s\r\n' % (outlet) )
                response = self.telnet.read_until(self.command_prompt, self.timeout)

    def turnOnAll(self):
        if self.telnet is not None and self.connected:
            self.turnOn(1)
            self.turnOn(2)
            self.turnOn(3)
            self.turnOn(4)
            self.turnOn(5)
            self.turnOn(6)
            self.turnOn(7)
            self.turnOn(8)

    def turnOff(self, outlet=-1):
        if self.telnet is not None and self.connected:
            if outlet >=1 and outlet <=8:
                self.telnet.write(b'Off %s\r\n' % (outlet) )
                response = self.telnet.read_until(self.command_prompt, self.timeout)

    def turnOffAll(self):
        if self.telnet is not None and self.connected:
            self.turnOffAll(1)
            self.turnOffAll(2)
            self.turnOffAll(3)
            self.turnOffAll(4)
            self.turnOffAll(5)
            self.turnOffAll(6)
            self.turnOffAll(7)
            self.turnOffAll(8)



