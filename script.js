document.addEventListener("DOMContentLoaded", function () {
  function updateCountdownAndNumber(serverTime) {
    // 设置初始倒计时时间
    let countdownTime = 30;

    // 更新倒计时和随机数字
    function updateCountdown() {
      document.getElementById("countdown").innerText = countdownTime;
      document.getElementById("randomNumber").innerText = getRandomNumber();

      // 减少倒计时时间
      countdownTime--;

      // 当倒计时为0时，重置倒计时时间和刷新随机数字
      if (countdownTime < 0) {
        countdownTime = 30;
      }
    }

    // 获取随机数字
    function getRandomNumber() {
      return Math.floor(Math.random() * 100);
    }

    // 初始化页面加载时的倒计时和随机数字
    updateCountdown();

    // 设置定时器，每秒更新一次倒计时和随机数字
    setInterval(updateCountdown, 1000);
  }

  // 向服务器请求当前时间
  function fetchServerTime() {
    fetch("/getServerTime") // 请替换为你的服务器端时间获取端点
      .then((response) => response.json())
      .then((data) => {
        updateCountdownAndNumber(data.serverTime);
      })
      .catch((error) => {
        console.error("Error fetching server time:", error);
      });
  }

  // 初始化页面时获取服务器时间
  fetchServerTime();
});
