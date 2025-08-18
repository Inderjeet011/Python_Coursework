# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 16:10:51 2016

@author: phil
"""

import socket
import os
import timeit
import logging

# Set up the logging
logging.basicConfig(
    format="%(asctime)s - %(message)s",
    level=logging.DEBUG,
)
logger = logging.getLogger(__name__)

# Parameters
# host = 'TBC'
host = '127.0.0.1'
port = 1234
repeats = 100  # Keep this <= 100, please!
timeout = 5  # Number of seconds until giving up on connection

def round_trip(skt):
    payload = os.urandom(1024)

    skt.sendall(payload)
    received_payload = skt.recv(1024)

    if received_payload != payload:
        raise IOError("We received an incorrect echo")

try:
    with socket.create_connection(address=(host, port), timeout=timeout) as skt:
        logger.info("Created connection")
        
        # Calculate average return time over multiple repeats
        total_time = 0
        for i in range(repeats):
            start_time = timeit.default_timer()
            round_trip(skt)
            end_time = timeit.default_timer()
            round_trip_time = (end_time - start_time) * 1000  # Convert to milliseconds
            total_time += round_trip_time
            logger.info("Completed trial {}: {:.2f} ms".format(i+1, round_trip_time))
        
        average_return_time = total_time / repeats
        logger.info("Average time taken: {:.2f} ms".format(average_return_time))
        
except ConnectionRefusedError as e:
    logger.error(
        "We could not create a socket connection to the "
        "remote echo server"
    )
    raise e

