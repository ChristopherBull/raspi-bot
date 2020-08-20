import 'mocha';
import { expect } from 'chai';
import index = require('../rpi_bot/index');
import Comms = require('../rpi_bot/comms/communication-manager');

describe('Program entry point', function () {
  after(function () {
    Comms.stopServer(Comms.CommunicationType.All);
    Comms.stopDiscoveryService();
  });

  it('should initialise without error', function () {
    expect(() => {
      index.initialise();
    }).to.not.throw(Error);
  });

  it('should initialise a second time without error', function () {
    expect(() => {
      index.initialise();
    }).to.not.throw(Error);
  });
});
