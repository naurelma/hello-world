from multiprocessing import Pool

def job(num):
    org = num +1
    num = num **num
    num = num /org
    return num


if __name__ == '__main__':
    p = Pool(processes=20)
    data = p.map(job, [i for i in range(20)])
    p.close()
    print(data)
