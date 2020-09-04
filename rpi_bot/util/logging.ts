import { createLogger, format, transports } from 'winston';

// Explicit log levels to use
const DEBUG =
  process.argv.indexOf('--debug') >= 0 || process.argv.indexOf('-d') >= 0;
// NB: Verbose log level - do not use "-v", which is typically for "--version"
const VERBOSE = process.argv.indexOf('--verbose') >= 0;

// Silent - No logging
const silent = process.argv.indexOf('--silent') >= 0;

// Testing - Reduced logging (e.g., warn and error only)
const TESTING = !silent && process.env.NODE_ENV === 'test';

// Determine which log level to use
let logLevel = 'info';
if (DEBUG) {
  logLevel = 'debug';
} else if (VERBOSE) {
  logLevel = 'verbose';
} else if (TESTING) {
  // Testing, so only show issues
  logLevel = 'warn';
}

const Logger = createLogger({
  level: logLevel,
  format: format.combine(
    format.timestamp({
      format: 'YYYY-MM-DD HH:mm:ss',
    }),
    format.errors({ stack: true }),
    format.splat(),
    format.json(),
  ),
  defaultMeta: { service: 'your-service-name' },
  transports: [
    // Write all logs with level `error` to `error.log`.
    new transports.File({ filename: 'logs/error.log', level: 'error' }),
    // Write all logs with level `info` to `combined.log`.
    new transports.File({ filename: 'logs/combined.log' }),
  ],
  silent: silent,
});

// If we're not in production then also log to the `console`
// with the colorized simple format.
if (process.env.NODE_ENV !== 'production') {
  Logger.add(
    new transports.Console({
      format: format.combine(format.colorize(), format.simple()),
      level: logLevel,
    }),
  );
}

// Logger setup complete
Logger.verbose('Logging initialised');
export default Logger;
