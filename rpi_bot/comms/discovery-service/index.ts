import dgram = require('dgram');
import net = require('net');
import { getStrAsNumberOrDefault } from '../../util/primitives';
import Logger from '../../util/logging';

/** Port number for the UDP Discovery service */
export const PORT_UDP_DISCOVERY: number = getStrAsNumberOrDefault(
  process.env.RPIBOT_DISCOVERY_PORT,
  9022,
);
/** Port number for the TCP response to a successful UDP Discovery */
export const PORT_TCP_RESPONSE = getStrAsNumberOrDefault(
  process.env.RPIBOT_RESPONSE_PORT,
  9023,
);
export const MSG_DISCOVER_ADDR = 'DISCOVER_RPIBOT_ADDR';

let server: dgram.Socket | undefined;

/**
 * Disables Discoverable Mode on this device.
 *
 * @returns {Promise<void>}
 */
export async function disable(): Promise<void> {
  return new Promise((resolve) => {
    if (server === undefined) {
      Logger.verbose('UDP Discovery - Disabled (was not running)');
      resolve();
    } else {
      server.close(() => {
        server = undefined;
        Logger.verbose('UDP Discovery - Disabled');
        resolve();
      });
    }
  });
}

/**
 * Places the device into Discoverable Mode.
 *
 * Waits for a UDP discovery packet from a potential client, then responds with
 * a short-lived TCP connection to confirm this devices' existence and
 * willingness to connect.
 */
export function enable(): void {
  if (server === undefined) {
    // Datagram module - UDP
    server = dgram.createSocket('udp4');
    server.bind(PORT_UDP_DISCOVERY);

    // On udp message received
    server.on('message', (message, rinfo) => {
      if (message.toString() === MSG_DISCOVER_ADDR) {
        Logger.log(
          'info',
          'UDP Discovery - Discovered (' + rinfo.address + ')',
        );
        // Respond to Discovery enquiry through a TCP socket
        const client = new net.Socket();
        client.on('error', (err: Error) => {
          Logger.error(err);
          Logger.verbose('UDP Discovery - Cleaning up after error');
          client.destroy();
          disable();
        });
        client.connect(PORT_TCP_RESPONSE, rinfo.address, () => {
          // No need to send message, just connect, as the connection meta data
          // (remote IP address) will be used to setup a new connection
          Logger.verbose(
            'UDP Discovery - Connected to requester and IP shared',
          );
          // Cleanup after connection
          client.destroy();
          disable();
        });
      }
    });

    // On udp server started and listening.
    server.on('listening', () => {
      // Debug output - IP and port
      const address = server?.address();
      Logger.log(
        'info',
        'UDP Discovery - Enabled - ' + address?.address + ':' + address?.port,
      );
    });
  }
}

/**
 * Checks if the Discovery Service is enabled.
 *
 * @returns {boolean} `true` if enabled, otherwise `false`.
 */
export function isEnabled(): boolean {
  return server !== undefined;
}

// Cleanup
process.on('SIGINT', () => {
  disable();
});
