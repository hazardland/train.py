import pandas as pd
from sklearn.preprocessing import MinMaxScaler

import color


def diff(n1, n2):
    if n2 is None:
        return color.cyan(' %9f') % n1

    if n1 > n2:
        return color.blue('+%9f') % (n1)
    elif n1 < n2:
        return color.red('-%9f') % (n1)
    else:
        return color.yellow(' %9f') % n1

    # if n2 is None:
    #     return color.black(' %9f') % 0

    # if n1 > n2:
    #     return color.blue('+%9f') % (n1 - n2)
    # elif n1 < n2:
    #     return color.red('-%9f') % (n2 - n1)
    # else:
    #     return color.black(' %9f') % 0

def outcome(n1, n2):
    result = [0, 0, 0]
    if n2 is None:
        return result
    if n1 > n2:
        result[0] = 1
    elif n1 < n2:
        result[1] = 1
    else:
        result[2] = 1
    return result

def prepare(file1_name, file2_name, file3_name):
    scaler = MinMaxScaler()

    # print(chart.plot(file1['close'][:130], {'height': 4, 'format':'{:8.0f}'}))
    file1 = pd.read_csv(file1_name)
    file1[['close']] = scaler.fit_transform(file1[['close']])
    file1[['volume']] = scaler.fit_transform(file1[['volume']])
    file1 = file1.set_index(['date'])

    file2 = pd.read_csv(file2_name)
    file2[['close']] = scaler.fit_transform(file2[['close']])
    file2[['volume']] = scaler.fit_transform(file2[['volume']])
    file2 = file2.set_index(['date'])

    file3 = pd.read_csv(file3_name)
    file3[['close']] = scaler.fit_transform(file3[['close']])
    file3[['volume']] = scaler.fit_transform(file3[['volume']])
    file3 = file3.set_index(['date'])

    history = []
    data = []
    target = []

    file1_close = None
    file2_close = None
    file3_close = None
    file1_volume = None
    file2_volume = None
    file3_volume = None

    i = 0
    backtrack = 60
    for index, file1_row in file1.iterrows():
        # print(color.cyan(index))
        #print(row)
        try:
            file2_row = file2.loc[index]
            file3_row = file3.loc[index]
            # print(color.yellow('%s found') % index)
        except:
            print(color.red('%s not found') % index)
            continue


        if len(history) >= backtrack:
            data.append(history[i-backtrack:i])
            #target.append(outcome(file1_row['close'], file1_close))
            target.append([file1_row['close']])

        print(
            str(i).rjust(3)+':',
            outcome(file1_row['close'], file1_close),
            diff(file1_row['close'], file1_close),
            diff(file1_row['volume'], file1_volume),
            diff(file2_row['close'], file2_close),
            diff(file2_row['volume'], file2_volume),
            diff(file3_row['close'], file3_close),
            diff(file3_row['volume'], file3_volume),
            ['%9f' % h[0] for h in data[i-backtrack]] if len(history) >= backtrack else '',
            target[i-backtrack] if len(history) >= backtrack else ''
            )


        file1_close = file1_row['close']
        file1_volume = file1_row['volume']
        file2_close = file2_row['close']
        file2_volume = file2_row['volume']
        file3_close = file3_row['close']
        file3_volume = file3_row['volume']
        history.append([file1_close, file1_volume, file2_close, file2_volume, file3_close, file3_volume])
        i += 1

    print(data[len(data)-1])
    print(color.cyan(target[len(target)-1]))

    return data, target
