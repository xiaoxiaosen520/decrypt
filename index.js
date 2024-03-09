const { exec } = require('child_process');

// 调用 Python 脚本
exec('python decrypt.py', (error, stdout, stderr) => {
  if (error) {
    console.error(`执行错误：${error.message}`);
    return;
  }
  if (stderr) {
    console.error(`错误输出：${stderr}`);
    return;
  }
  console.log(`Python 脚本输出：${stdout}`);
});
