import os, glob, json

root_dir = './newstext'
dic_file = root_dir+'/word_dic.json'
data_file = root_dir+'/data.json'
data_file_min = root_dir+'/data_mini.json'

word_dict = { '_MAX':0 }
def text_to_ids(text):
    text = text.strip()
    words = text.split(' ')
    result = []
    for n in words:
        n = n.strip()
        if n == '': 
            continue
        if not n in word_dict:
            wid = word_dic[n] = word_dic['_MAX']
            word_dict['_MAX'] += 1
            print(wid, n)
        else:
            wid = word_dic[n]
        result.append(wid)
    return result

def file_to_ids(fname):
    with open(fname, 'r') as f:
        text = f.read()
        return text_to_ids(text)

def register_dic():
    files = glob.glob(root_dir+'/*/*.wakati', recursive=True)
    for i in files:
        file_to_ids(i)

def count_file_freq(fname):
    cnt = [0 for n in range(word_dic['_MAX'])]
    with open(fname, 'r') as f:
        text = f.read().strip()
        ids = text_to_ids(text)
        for wid in ids:
            cnt[wid] += 1
    return cnt

def count_freq(limit = 0):
    X = []
    Y = []
    max_words = word_dic['_MAX']
    cat_names = []
    for cat in os.listdir(root_dir):
        cat_dir = root_dir+'/'+cat
        if not os.path.isdir(cat_dir):
            continue
        cat_idx = len(cat_names)
        cat_names.append(cat)
        files = glob.glob(cat_dir+'/*.wakati')
        i=0
        for path in files:
            print(path)
            cnt = count_file_freq(path)
            X.append(cnt)
            Y.append(cat_idx)
            if limit > 0:
                if i > limit:
                    break
                i += 1
    return X, Y

if os.path.exists(dic_file):
    word_dic = json.load(open(dic_file))
else:
    register_dic()
    json.dump(word_dic, open(dic_file, 'w'))

X, Y = count_freq(20)
json.dump({'X':X, 'Y':Y}, open(data_file_min, 'w'))
X, Y = count_freq()
json.dump({'X':X, 'Y':Y}, open(data_file, 'w'))
print('ok!')
