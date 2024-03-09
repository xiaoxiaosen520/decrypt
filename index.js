const { exec } = require('child_process');

// launch Python 
exec('python decrypt.py', (error, stdout, stderr) => {
  if (error) {
    console.error(`fail：${error.message}`);
    return;
  }
  if (stderr) {
    console.error(`fial log：${stderr}`);
    return;
  }
  console.log(`Python succees：${stdout}`);
});
