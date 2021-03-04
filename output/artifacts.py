{\rtf1\ansi\ansicpg1252\cocoartf2577
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Monaco;}
{\colortbl;\red255\green255\blue255;\red199\green200\blue201;\red22\green21\blue22;}
{\*\expandedcolortbl;;\cssrgb\c81961\c82353\c82745;\cssrgb\c11373\c10980\c11373\c3922;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl360\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import os\cb1 \
\cb3 import time\cb1 \
\cb3 from cnvrg import Experiment\cb1 \
\cb3 os.system("mkdir -p testfiles")\cb1 \
\cb3 e = Experiment()\cb1 \
\cb3 for commit in range(5):\cb1 \
\cb3     file_list = []\cb1 \
\cb3     for i in range(25):\cb1 \
\cb3         with open(f"testfiles/filet\{i\}.txt", 'w+') as file:\cb1 \
\cb3             file.write('hello')\cb1 \
\cb3         with open(f"testfiles/filet\{i\}.txt_tags.yml", 'w+') as yml:\cb1 \
\cb3             yml.write(f"---\\nid: \\"\{i\}\\"\\nsource: \\"yann lecun\\"")\
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb1 \
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3         file_list.append(f"testfiles/filet\{i\}.txt")\cb1 \
\cb3         file_list.append(f"testfiles/filet\{i\}.txt_tags.yml")\
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb1 \
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3     e.log_artifacts(file_list)\cb1 \
\cb3     time.sleep(5)\cb1 \
\cb3     print(f"commited: \{commit\}")\
}