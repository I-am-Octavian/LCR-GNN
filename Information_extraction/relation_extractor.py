import os
import subprocess
import glob
import pandas as pd
from tqdm import tqdm

input_path = '/home/adi/Dev/CaseGNN/DATASET/Relations-issue'

def Stanford_Relation_Extractor():
    
    print('Relation Extraction Started')
    for f in tqdm(glob.glob(input_path+"/kg/*.txt")):
        if os.path.exists(f + '-out.csv'):
            continue
        else:
            os.chdir('./Information_extraction/stanford-openie')

            p = subprocess.Popen(['./process_large_corpus.sh',f,f + '-out.csv'], stdout=subprocess.PIPE)
            output, err = p.communicate()
            
            os.chdir( '../..')
   

    print('Relation Extraction Completed')


if __name__ == '__main__':
    Stanford_Relation_Extractor()
