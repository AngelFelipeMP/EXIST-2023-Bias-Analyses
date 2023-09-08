import os
#Hiper-parameters
EPOCHS = 10 #10
MAX_LEN = 100 # 100 
DROPOUT = 0.3
LR = 3e-5 #5e-6, 1e-5, 3e-5, 5e-5
BATCH_SIZE = 20 #24
TRANSFORMERS = ['bert-base-multilingual-uncased','xlm-roberta-base']
# TRANSFORMERS = ['bert-base-multilingual-uncased','xlm-roberta-base','infoxlm-base']

N_ROWS=None #16
SEED = 17
CODE_PATH = os.getcwd()
REPO_PATH = '/'.join(CODE_PATH.split('/')[0:-1])
DATA_PATH = REPO_PATH + '/' + 'data' 
PACKAGE_PATH = REPO_PATH + '/' + 'package'
DATA_DEV_PATH = PACKAGE_PATH + '/' + 'dev/EXIST2023_dev' + '.json'
DATA_TRAIN_PATH = PACKAGE_PATH + '/' + 'training/EXIST2023_training' + '.json'
DATA_TEST_PATH = PACKAGE_PATH + '/' + 'test/EXIST2023_test_clean' + '.json'
LABEL_GOLD_PATH = PACKAGE_PATH + '/' + 'evaluation/golds'

DATA = 'EXIST2023' 
DATA_URL = 'https://drive.google.com/file/d/11WxMMTyZibk6hWNSp2UeVFTllFcgfs52/view?usp=share_link'

LABELS = ['task1', 'task2','task3'] #['task1', 'task2','task3']
COLUMN_TEXT = 'tweet'
COLUMN_LABELS = 'soft_label_'
DATASET_INDEX = 'id_EXIST'
UNITS = {'task1': 2, 'task2': 3, 'task3': 5}

DATASET_TRAIN = 'EXIST2023_training.csv'
DATASET_DEV = 'EXIST2023_dev.csv'
DATASET_TEST = 'EXIST2023_test.csv'
DATASET_TRAIN_DEV = 'EXIST2023_training-dev.csv'

DEVICE = 'max' # None 'max' 'cpu' 'cuda:0' 'cuda:1'
TRAIN_WORKERS = 10
VAL_WORKERS = 10
LOGS_PATH = REPO_PATH + '/' + 'logs'



# DATASET_COLUMNS = [DATASET_INDEX, *DATASET_TEXT] + LABELS
# DATASET_CLASSES = {
#     DATASET_COLUMNS[2]:{'NO': 0, 'YES':1}, 
#     DATASET_COLUMNS[3]:{'NO':-1,'DIRECT':0,'REPORTED':1, 'JUDGEMENTAL':2},
#     DATASET_COLUMNS[4]:{'NO':-1,'IDEOLOGICAL-INEQUALITY':0,'STEREOTYPING-DOMINANCE':1, 'OBJECTIFICATION':2, 'SEXUAL-VIOLENCE':3, 'MISOGYNY-NON-SEXUAL- VIOLENCE':4}
#                 }