import copy
import time
import subprocess

from multiprocessing import Process


process_num = 2

data = []
with open('data.tsv', 'r', encoding='utf-8') as fr:
    for line in fr.readlines():
        text, label = line.replace('\n', '').split('\t')
        data.append({'text':text, 'label':label})

start_time = time.time()

def parallel_preprocessing(idx, data):

    print('{} process started'.format(idx))

    def preprocessing(text):
        ### add your preprocessing ###
        return text + ' preprocessed'

    with open('data_preprocessed_{}.tsv'.format(idx), 'w', encoding='utf-8') as fw:
        for line in data:
            text = line['text']
            label = line['label']
            fw.write(text + '\t' + preprocessing(text) + '\t' + label + '\n')
    
    print('{} process finished'.format(idx))


processes = []

divide = int(len(data)/process_num)
for i in range(process_num):
    start = i*divide
    end = len(data) if i+1 == process_num else (i+1)*divide
    process = Process(target=parallel_preprocessing, args=(i, copy.deepcopy(data[start:end])))
    processes.append(process)
    process.start()

for p in processes:
    p.join()

end_time = time.time()

print('Finished preprocessing in {} secs'.format(end_time - start_time))

print('Start merging temp files')
temp_files = ' '.join(['data_preprocessed_{}.tsv'.format(i) for i in range(process_num)])
subprocess.call('cat {} > data_preprocessed.tsv'.format(temp_files), shell=True)
subprocess.call('rm {}'.format(temp_files), shell=True)
print('Finish merging temp files')

