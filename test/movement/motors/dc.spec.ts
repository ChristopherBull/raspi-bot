import 'mocha';
import { DCMotor } from '../../../rpi_bot/movement/motors/dc';
import { expect } from 'chai';
import { MotorMotionType } from '../../../rpi_bot/movement/movement-manager';

describe('Motor: DC', function () {
  let motor: DCMotor;

  before(function () {
    motor = new DCMotor(1, 2, 3);
  });

  it('should init in a stopped state', function () {
    const state = motor.getCurrentState();
    expect(state).to.equal(MotorMotionType.Stop);
  });

  it('should move clockwise', function () {
    motor.clockwise();
    const state = motor.getCurrentState();
    expect(state).to.equal(MotorMotionType.Clockwise);
  });

  it('should move counter-clockwise', function () {
    motor.counterClockwise();
    const state = motor.getCurrentState();
    expect(state).to.equal(MotorMotionType.CounterClockwise);
  });

  it('should stop moving', function () {
    motor.stop();
    const state = motor.getCurrentState();
    expect(state).to.equal(MotorMotionType.Stop);
  });
});
