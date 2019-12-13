# coding:utf-8
import random
import fun


def get_key():
    RSA_key = {}
    # 生成2个与质数数组都互质的大素数
    prime_arr = fun.get_rand_prime_arr(2)
    p = prime_arr[0]
    q = prime_arr[1]
    # 判断是否相等
    while True:
        if p != q:
            break
        else:
            prime_arr = fun.get_rand_prime_arr(2)
            p = prime_arr[0]
            q = prime_arr[1]
    # 计算乘积
    n = p * q
    # 计算欧拉函数
    s = (p - 1) * (q - 1)
    # 随机选择一个与s互质的整数
    while True:
        e = random.randint(1, s)
        if fun.mutual_quality(e, s) == 1:
            break
    # 扩展欧几里得算法计算e对于s的反模d，即ed - 1 = kφ(n)，k为整数,ed/φ(n)余1
    d = fun.mod_inverse(e, s)
    # print "p = ", p
    # print "q = ", q
    print "私钥"
    print "n = ", n
    print "e = ", e
    print "公钥"
    print "n = ", n
    print "d = ", d
    # [n,e]为公钥
    puk = [n, e]
    # [n,d]为私钥
    prk = [n, d]
    RSA_key['puk'] = puk
    RSA_key['prk'] = prk
    return RSA_key


if __name__ == '__main__':
    key = get_key()
    print "输入一个小于 ", len(str(key['puk'][0])), "位"
    print "同时比", key['puk'][0], "小的数字:"
    message = int(input())
    if len(str(message)) > len(str(key['puk'][0])) or message > key['puk'][0]:
        print "不符合规则，请重新输入"
        message = int(input())
    # m^e - c = kn，k为整数，m为明文，c为加密结果，m^e/n余c
    # 快速幂模运算
    secret = fun.quick_pow_mod(message, key['puk'][1], key['puk'][0])
    print "加密后:", secret
    print "密文长度:",len(str(secret))
    # c^d - m = kn，k为整数，m为明文，c为密文，c^d/n余m
    message = fun.quick_pow_mod(secret, key['prk'][1], key['prk'][0])
    print "解密后:", message
