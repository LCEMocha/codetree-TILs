import collections
import copy

table = collections.defaultdict(list)
customer_remain = {}

def table_spin(l):
    global table
    global customer_remain
    for k,v in table.items():
        for i in range(len(v)):
            if v[i] == l-1:
                v[i] = 0
            else:
                v[i] += 1
    # 돌아온 초밥 계산
    copy_table = copy.deepcopy(table)
    for k,v in copy_table.items():
        for i in v:
            if customer_remain.get((i, k), 0) != 0 and customer_remain[(i, k)] >= 1:
                customer_remain[(i, k)] -= 1
                table[k].remove(i)
                if customer_remain[(i, k)] == 0:
                    del customer_remain[(i, k)]

def sushi(temp):
    global table
    table_num = int(temp[2])
    sushi_name = temp[3]
    table[sushi_name].append(table_num)
    # 새로 놓인 초밥
    copy_table = copy.deepcopy(table)
    if customer_remain.get((table_num, sushi_name), 0) != 0:
        for v in copy_table[sushi_name]:
            if v == table_num and customer_remain[(table_num, sushi_name)] >= 1:
                customer_remain[(table_num, sushi_name)] -= 1
                table[sushi_name].remove(v)
        if customer_remain[(table_num, sushi_name)] == 0:
            del customer_remain[(table_num, sushi_name)]


def customer(temp):
    global table
    global customer_remain
    table_num = int(temp[2])
    customer_name = temp[3]
    should_eat = int(temp[4])
    customer_remain[(table_num, customer_name)] = should_eat
    copy_table = copy.deepcopy(table)
    if table[customer_name] and table_num in table[customer_name]:
        for v in copy_table[customer_name]:
            if v == table_num and customer_remain[(table_num, customer_name)] >= 1:
                customer_remain[(table_num, customer_name)] -= 1
                table[customer_name].remove(v)
    if customer_remain[(table_num, customer_name)] == 0:
        del customer_remain[(table_num, customer_name)]


def picture():
    global table
    global customer_remain
    count_sushi = 0
    count_customer = 0
    for k in table.keys():
        if table[k]:
            count_sushi += len(table[k])
    count_customer += len(customer_remain)
    return count_customer, count_sushi


def main():
    L, Q = map(int, input().split())
    last_t = 1
    current_t = 1
    for i in range(Q):
        temp = list(input().split())
        current_t = int(temp[1])
        #print('t:', current_t, temp)
        for _ in range(current_t - last_t):
            table_spin(L)
        last_t = int(temp[1])
        if temp[0] == '100':
            sushi(temp)
            #print('100 table:', table)
            #print('100 customer:', customer_remain)
        if temp[0] == '200':
            customer(temp)
            #print('200 table:', table)
            #print('200 customer:', customer_remain)
        if temp[0] == '300':
            sushi_left, customer_left = picture()
            #print('300 table:', table)
            #print('300 customer:', customer_remain)
            print(sushi_left, customer_left)


if __name__ == '__main__':
    main()