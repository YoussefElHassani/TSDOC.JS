import subprocess
import shlex
import threading


class ShCommand:
    """
    This class can be used to run a shell command.  You can optionally provide
    it with a timeout and it will kill the shell command if it doesn't complete
    before timeout.

    e.g.
    ShCommand("command arg1 arg2", logger, "RelevantLoggingPrefix", 10).run()
    """
    def __init__(self, cmd, logger, log_prefix, timeout=None):
        """
        `cmd`: The command to run
        `logger`: The logger to use for logging various information.
        `log_prefix`: The prefix to apply to each log statement.
        `timeout`: The number of seconds to wait for the command to finish
                execution. After timeout seconds have passed, a terminate
                signal is send to the command, followed by a kill signal.
        """
        self.cmd = shlex.split(str(cmd))
        self.logger = logger
        self.log_prefix = log_prefix
        self.timeout = timeout
        self.process = None
        self.stdout = None
        self.stderr = None

    def target(self):
        self.logger.info("%s: Running command: %s", self.log_prefix, str(self.cmd))
        self.process = subprocess.Popen(self.cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        self.logger.info("%s: pid: %s", self.log_prefix, self.process.pid)
        self.stdout, self.stderr = self.process.communicate()
        if self.process.returncode != 0:
            self.logger.error("%s: Command with pid %s done with return code: %s",
                    self.log_prefix, self.process.pid, self.process.returncode)
        else:
            self.logger.info("%s: Command with pid %s done with return code: %s",
                    self.log_prefix, self.process.pid, self.process.returncode)

    def run(self):
        thread = threading.Thread(target=self.target)
        thread.start()

        thread.join(self.timeout)
        if thread.is_alive():
            self.process.terminate()
            # Should I wait for a second here?
            self.process.kill()
            self.logger.error('%s: Process with pid %s got timed out with the timeout set to be %s',
                    self.log_prefix, self.process.pid, self.timeout)
            # The thread should now join immediately. Wait some more and then move on.
            thread.join(self.timeout)

        if self.stdout:
            self.logger.debug("%s: STDOUT of command with pid %s:",
                    self.log_prefix, self.process.pid)
            self.logger.debug(self.stdout)
        if self.stderr:
            self.logger.debug("%s: STDERR of command with pid %s:",
                    self.log_prefix, self.process.pid)
            self.logger.debug(self.stderr)

        return self.process.returncode, self.stdout, self.stderr