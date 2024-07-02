from netmiko import SSHDetect, ConnectHandler

from netmiko.exceptions import (
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
    ConfigInvalidException,
    ReadException,
    ReadTimeout,
    NetMikoTimeoutException,
    NetMikoAuthenticationException,
)

def connect_to_device(device_connection_details, logger):
    '''     
    :params
        device_connection_details: dictionary that contains the details about the device we are connecting
        logger: logger that captures the events in the code execution
        return: e, Any error generated. ssh_connection, object with the SSL connection
    '''
    try:
        net_connection = ConnectHandler(**device_connection_details)
    except ConfigInvalidException as error:
        logger.error(f'{device_connection_details["ip"]}: Configuration not accepted by the device {error}')
        return False
    except NetMikoTimeoutException as error:
        logger.error(f'{device_connection_details["ip"]}: Connection timeout {error}')
        return False
    except NetMikoAuthenticationException as error:
        logger.error(f'{device_connection_details["ip"]}: unable to login to the device {error}')
        return False
    except :
        logger.error(f'{device_connection_details["ip"]}, unupported platform')
        return False
    
    try:
        net_connection.enable()
        return net_connection
    except (NetMikoTimeoutException, NetMikoAuthenticationException, NetmikoAuthenticationException,
            NetmikoTimeoutException, ReadTimeout, ReadException) as error:
        logger.error(f'{device_connection_details["ip"]}: Connection Refused {error}')
        return False
    except ConfigInvalidException as error:
        logger.error(f'{device_connection_details["ip"]}: Configuration not accepted by the device {error}')
        return False
    except :
        logger.error(f'{device_connection_details["ip"]}: Unknown error ')
        return False

        