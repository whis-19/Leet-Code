var distMoney = function (money, children) {
    if (money < children) return -1;

    let ans = 0;
    for (let j = 1; j <= children; j++) {
        let leftmoney = money - 8;
        let leftchildren = children - j;

        if (leftmoney >= leftchildren) {
            money = leftmoney;
            ans++;
        } else {
            leftchildren = children - j + 1;

            if (leftchildren === 1 && money === 4) ans--;
            money = 0;
            break;
        }
    }
    if (money > 0) ans--;
    return ans;
}

