const {spawn} = require('child_process');

function startProcess(command, args) {
  console.log('Start Process: ', command);
  const proc = spawn(command, args || []);
  listenEvent(proc);
  return proc;
}

function listenEvent(proc) {
  proc.stderr.on('data', (data) => {
    console.log(data.toString());
  });
  proc.on('disconnect', () => {
    console.log('process stopped gracefully');
  });
  proc.on('close', () => {
    console.log('process stopped');
  });
}

function stopProcess(proc) {
  console.log('Kill Process With Signal SIGTERM');
  proc.kill('SIGTERM')
}

function clearIntervalTimer(timer) {
  if (timer) {
    clearInterval(timer);
    timer = null;
  }
}

function clearTimeoutTimer(timer) {
  if (timer) {
    clearTimeout(timer);
    timer = null;
  }
}

function loopSchedule(when, what) {
  const {hours, minutes, seconds, interval} = when;
  let [tTimer, iTimer] = [null, null];
  const now = new Date();
  const target = new Date(now.getFullYear(), now.getMonth(), now.getDay() + 1, hours, minutes, seconds);
  const waitTime = target.getTime() - now.getTime();
  if (waitTime < 0) {
    console.log('started');
    what();
    if (interval) {
      iTimer = setInterval(() => {
        console.log('run in interval: ', interval);
        what();
      }, interval)
    }
  } else {
    tTimer = setTimeout(() => {
      console.log('started');
      what();
      clearTimeoutTimer(tTimer);
      if (interval) {
        iTimer = setInterval(() => {
          console.log('run in interval: ', interval);
          what();
        }, interval)
      }
    }, waitTime);
    clearIntervalTimer(iTimer);
  }
}

function main() {
  let command = null;
  // first start at 19:25:00, next is 19:35:00
  // first stop at 19:30:00, next is 19:40:00
  // work 10 5 minutes, rest for 5 minutes

  loopSchedule({hours: 19, minutes: 36, seconds: 0, interval: 10 * 1000}, () => {
    command = startProcess('./runforever.sh')
  });
  loopSchedule({hours: 19, minutes: 36, seconds: 30, interval: 10 * 1000}, () => stopProcess(command));
}

main();
