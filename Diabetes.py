{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv('C:/Users/Balaji/Downloads/diabetes_data_upload.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Polyuria</th>\n",
       "      <th>Polydipsia</th>\n",
       "      <th>sudden weight loss</th>\n",
       "      <th>weakness</th>\n",
       "      <th>Polyphagia</th>\n",
       "      <th>Genital thrush</th>\n",
       "      <th>visual blurring</th>\n",
       "      <th>Itching</th>\n",
       "      <th>Irritability</th>\n",
       "      <th>delayed healing</th>\n",
       "      <th>partial paresis</th>\n",
       "      <th>muscle stiffness</th>\n",
       "      <th>Alopecia</th>\n",
       "      <th>Obesity</th>\n",
       "      <th>class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>58</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>41</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>45</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>60</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5</td>\n",
       "      <td>55</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>6</td>\n",
       "      <td>57</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>7</td>\n",
       "      <td>66</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>8</td>\n",
       "      <td>67</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>9</td>\n",
       "      <td>70</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Age Gender Polyuria Polydipsia sudden weight loss weakness Polyphagia  \\\n",
       "0   40   Male       No        Yes                 No      Yes         No   \n",
       "1   58   Male       No         No                 No      Yes         No   \n",
       "2   41   Male      Yes         No                 No      Yes        Yes   \n",
       "3   45   Male       No         No                Yes      Yes        Yes   \n",
       "4   60   Male      Yes        Yes                Yes      Yes        Yes   \n",
       "5   55   Male      Yes        Yes                 No      Yes        Yes   \n",
       "6   57   Male      Yes        Yes                 No      Yes        Yes   \n",
       "7   66   Male      Yes        Yes                Yes      Yes         No   \n",
       "8   67   Male      Yes        Yes                 No      Yes        Yes   \n",
       "9   70   Male       No        Yes                Yes      Yes        Yes   \n",
       "\n",
       "  Genital thrush visual blurring Itching Irritability delayed healing  \\\n",
       "0             No              No     Yes           No             Yes   \n",
       "1             No             Yes      No           No              No   \n",
       "2             No              No     Yes           No             Yes   \n",
       "3            Yes              No     Yes           No             Yes   \n",
       "4             No             Yes     Yes          Yes             Yes   \n",
       "5             No             Yes     Yes           No             Yes   \n",
       "6            Yes              No      No           No             Yes   \n",
       "7             No             Yes     Yes          Yes              No   \n",
       "8            Yes              No     Yes          Yes              No   \n",
       "9             No             Yes     Yes          Yes              No   \n",
       "\n",
       "  partial paresis muscle stiffness Alopecia Obesity     class  \n",
       "0              No              Yes      Yes     Yes  Positive  \n",
       "1             Yes               No      Yes      No  Positive  \n",
       "2              No              Yes      Yes      No  Positive  \n",
       "3              No               No       No      No  Positive  \n",
       "4             Yes              Yes      Yes     Yes  Positive  \n",
       "5              No              Yes      Yes     Yes  Positive  \n",
       "6             Yes               No       No      No  Positive  \n",
       "7             Yes              Yes       No      No  Positive  \n",
       "8             Yes              Yes       No     Yes  Positive  \n",
       "9              No               No      Yes      No  Positive  "
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Age                   0\n",
       "Gender                0\n",
       "Polyuria              0\n",
       "Polydipsia            0\n",
       "sudden weight loss    0\n",
       "weakness              0\n",
       "Polyphagia            0\n",
       "Genital thrush        0\n",
       "visual blurring       0\n",
       "Itching               0\n",
       "Irritability          0\n",
       "delayed healing       0\n",
       "partial paresis       0\n",
       "muscle stiffness      0\n",
       "Alopecia              0\n",
       "Obesity               0\n",
       "class                 0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "df1=df.copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1d38807f2c8>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.scatterplot(x=df['Age'],y=df['class'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Positive    320\n",
       "Negative    200\n",
       "Name: class, dtype: int64"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['class'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "df['class_1']=df['class'].replace({'Positive ':'1','Negative':'0'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['class_1']=df['class_1'].astype(int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 520 entries, 0 to 519\n",
      "Data columns (total 18 columns):\n",
      "Age                   520 non-null int64\n",
      "Gender                520 non-null object\n",
      "Polyuria              520 non-null object\n",
      "Polydipsia            520 non-null object\n",
      "sudden weight loss    520 non-null object\n",
      "weakness              520 non-null object\n",
      "Polyphagia            520 non-null object\n",
      "Genital thrush        520 non-null object\n",
      "visual blurring       520 non-null object\n",
      "Itching               520 non-null object\n",
      "Irritability          520 non-null object\n",
      "delayed healing       520 non-null object\n",
      "partial paresis       520 non-null object\n",
      "muscle stiffness      520 non-null object\n",
      "Alopecia              520 non-null object\n",
      "Obesity               520 non-null object\n",
      "class                 520 non-null object\n",
      "class_1               520 non-null int32\n",
      "dtypes: int32(1), int64(1), object(16)\n",
      "memory usage: 71.2+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>class_1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>Age</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.108679</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>class_1</td>\n",
       "      <td>0.108679</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              Age   class_1\n",
       "Age      1.000000  0.108679\n",
       "class_1  0.108679  1.000000"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Age', 'Gender', 'Polyuria', 'Polydipsia', 'sudden weight loss',\n",
       "       'weakness', 'Polyphagia', 'Genital thrush', 'visual blurring',\n",
       "       'Itching', 'Irritability', 'delayed healing', 'partial paresis',\n",
       "       'muscle stiffness', 'Alopecia', 'Obesity', 'class', 'class_1'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 520 entries, 0 to 519\n",
      "Data columns (total 18 columns):\n",
      "Age                   520 non-null int64\n",
      "Gender                520 non-null object\n",
      "Polyuria              520 non-null object\n",
      "Polydipsia            520 non-null object\n",
      "sudden weight loss    520 non-null object\n",
      "weakness              520 non-null object\n",
      "Polyphagia            520 non-null object\n",
      "Genital thrush        520 non-null object\n",
      "visual blurring       520 non-null object\n",
      "Itching               520 non-null object\n",
      "Irritability          520 non-null object\n",
      "delayed healing       520 non-null object\n",
      "partial paresis       520 non-null object\n",
      "muscle stiffness      520 non-null object\n",
      "Alopecia              520 non-null object\n",
      "Obesity               520 non-null object\n",
      "class                 520 non-null object\n",
      "class_1               520 non-null int32\n",
      "dtypes: int32(1), int64(1), object(16)\n",
      "memory usage: 71.2+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_nw=pd.get_dummies(data=df,columns=['Gender', 'Polyuria', 'Polydipsia', 'sudden weight loss',\n",
    "                                      'weakness', 'Polyphagia', 'Genital thrush', 'visual blurring',\n",
    "                                      'Itching', 'Irritability', 'delayed healing', 'partial paresis',\n",
    "                                      'muscle stiffness', 'Alopecia', 'Obesity', 'class'],drop_first=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_nw['Target']=df['class_1']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_nw.drop('class_Negative',axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Age', 'class_1', 'Gender_Male', 'Polyuria_Yes', 'Polydipsia_Yes',\n",
       "       'sudden weight loss_Yes', 'weakness_Yes', 'Polyphagia_Yes',\n",
       "       'Genital thrush_Yes', 'visual blurring_Yes', 'Itching_Yes',\n",
       "       'Irritability_Yes', 'delayed healing_Yes', 'partial paresis_Yes',\n",
       "       'muscle stiffness_Yes', 'Alopecia_Yes', 'Obesity_Yes', 'Target'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_nw.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.model_selection import KFold,cross_val_score,GridSearchCV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=df_nw.drop(['Target','class_1'],axis=1)\n",
    "y=df_nw['Target']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [],
   "source": [
    "log_reg=LogisticRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [],
   "source": [
    "Kfold=KFold(shuffle=True,n_splits=3,random_state=0)\n",
    "score=cross_val_score(log_reg,x,y,cv=Kfold,scoring='roc_auc')\n",
    "BE_log_reg=np.mean(1-score)\n",
    "VE_log_reg=np.std(score,ddof=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bias error 0.02498140206880935 Var error 0.003075096493024804 score 0.9750185979311906\n"
     ]
    }
   ],
   "source": [
    "print('bias error',BE_log_reg,'Var error',VE_log_reg,'score',np.mean(score))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Optimization terminated successfully.\n",
      "         Current function value: 0.165053\n",
      "         Iterations 10\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<table class=\"simpletable\">\n",
       "<caption>Logit Regression Results</caption>\n",
       "<tr>\n",
       "  <th>Dep. Variable:</th>        <td>Target</td>      <th>  No. Observations:  </th>   <td>   520</td>  \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Model:</th>                 <td>Logit</td>      <th>  Df Residuals:      </th>   <td>   503</td>  \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Method:</th>                 <td>MLE</td>       <th>  Df Model:          </th>   <td>    16</td>  \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Date:</th>            <td>Fri, 07 Aug 2020</td> <th>  Pseudo R-squ.:     </th>   <td>0.7523</td>  \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Time:</th>                <td>19:19:24</td>     <th>  Log-Likelihood:    </th>  <td> -85.827</td> \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>converged:</th>             <td>True</td>       <th>  LL-Null:           </th>  <td> -346.46</td> \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Covariance Type:</th>     <td>nonrobust</td>    <th>  LLR p-value:       </th> <td>1.067e-100</td>\n",
       "</tr>\n",
       "</table>\n",
       "<table class=\"simpletable\">\n",
       "<tr>\n",
       "             <td></td>               <th>coef</th>     <th>std err</th>      <th>z</th>      <th>P>|z|</th>  <th>[0.025</th>    <th>0.975]</th>  \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>const</th>                  <td>    2.7466</td> <td>    1.075</td> <td>    2.554</td> <td> 0.011</td> <td>    0.639</td> <td>    4.854</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Age</th>                    <td>   -0.0512</td> <td>    0.025</td> <td>   -2.017</td> <td> 0.044</td> <td>   -0.101</td> <td>   -0.001</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Gender_Male</th>            <td>   -4.3512</td> <td>    0.598</td> <td>   -7.274</td> <td> 0.000</td> <td>   -5.524</td> <td>   -3.179</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Polyuria_Yes</th>           <td>    4.4395</td> <td>    0.705</td> <td>    6.295</td> <td> 0.000</td> <td>    3.057</td> <td>    5.822</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Polydipsia_Yes</th>         <td>    5.0704</td> <td>    0.829</td> <td>    6.117</td> <td> 0.000</td> <td>    3.446</td> <td>    6.695</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>sudden weight loss_Yes</th> <td>    0.1903</td> <td>    0.548</td> <td>    0.348</td> <td> 0.728</td> <td>   -0.883</td> <td>    1.264</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>weakness_Yes</th>           <td>    0.8171</td> <td>    0.537</td> <td>    1.522</td> <td> 0.128</td> <td>   -0.235</td> <td>    1.869</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Polyphagia_Yes</th>         <td>    1.1938</td> <td>    0.534</td> <td>    2.238</td> <td> 0.025</td> <td>    0.148</td> <td>    2.239</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Genital thrush_Yes</th>     <td>    1.8637</td> <td>    0.553</td> <td>    3.368</td> <td> 0.001</td> <td>    0.779</td> <td>    2.948</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>visual blurring_Yes</th>    <td>    0.9159</td> <td>    0.651</td> <td>    1.406</td> <td> 0.160</td> <td>   -0.360</td> <td>    2.192</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Itching_Yes</th>            <td>   -2.8029</td> <td>    0.673</td> <td>   -4.167</td> <td> 0.000</td> <td>   -4.121</td> <td>   -1.485</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Irritability_Yes</th>       <td>    2.3407</td> <td>    0.591</td> <td>    3.964</td> <td> 0.000</td> <td>    1.183</td> <td>    3.498</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>delayed healing_Yes</th>    <td>   -0.3916</td> <td>    0.550</td> <td>   -0.712</td> <td> 0.476</td> <td>   -1.470</td> <td>    0.686</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>partial paresis_Yes</th>    <td>    1.1593</td> <td>    0.525</td> <td>    2.209</td> <td> 0.027</td> <td>    0.131</td> <td>    2.188</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>muscle stiffness_Yes</th>   <td>   -0.7288</td> <td>    0.580</td> <td>   -1.256</td> <td> 0.209</td> <td>   -1.866</td> <td>    0.408</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Alopecia_Yes</th>           <td>    0.1504</td> <td>    0.620</td> <td>    0.242</td> <td> 0.808</td> <td>   -1.065</td> <td>    1.366</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Obesity_Yes</th>            <td>   -0.2890</td> <td>    0.544</td> <td>   -0.531</td> <td> 0.595</td> <td>   -1.356</td> <td>    0.778</td>\n",
       "</tr>\n",
       "</table><br/><br/>Possibly complete quasi-separation: A fraction 0.24 of observations can be<br/>perfectly predicted. This might indicate that there is complete<br/>quasi-separation. In this case some parameters will not be identified."
      ],
      "text/plain": [
       "<class 'statsmodels.iolib.summary.Summary'>\n",
       "\"\"\"\n",
       "                           Logit Regression Results                           \n",
       "==============================================================================\n",
       "Dep. Variable:                 Target   No. Observations:                  520\n",
       "Model:                          Logit   Df Residuals:                      503\n",
       "Method:                           MLE   Df Model:                           16\n",
       "Date:                Fri, 07 Aug 2020   Pseudo R-squ.:                  0.7523\n",
       "Time:                        19:19:24   Log-Likelihood:                -85.827\n",
       "converged:                       True   LL-Null:                       -346.46\n",
       "Covariance Type:            nonrobust   LLR p-value:                1.067e-100\n",
       "==========================================================================================\n",
       "                             coef    std err          z      P>|z|      [0.025      0.975]\n",
       "------------------------------------------------------------------------------------------\n",
       "const                      2.7466      1.075      2.554      0.011       0.639       4.854\n",
       "Age                       -0.0512      0.025     -2.017      0.044      -0.101      -0.001\n",
       "Gender_Male               -4.3512      0.598     -7.274      0.000      -5.524      -3.179\n",
       "Polyuria_Yes               4.4395      0.705      6.295      0.000       3.057       5.822\n",
       "Polydipsia_Yes             5.0704      0.829      6.117      0.000       3.446       6.695\n",
       "sudden weight loss_Yes     0.1903      0.548      0.348      0.728      -0.883       1.264\n",
       "weakness_Yes               0.8171      0.537      1.522      0.128      -0.235       1.869\n",
       "Polyphagia_Yes             1.1938      0.534      2.238      0.025       0.148       2.239\n",
       "Genital thrush_Yes         1.8637      0.553      3.368      0.001       0.779       2.948\n",
       "visual blurring_Yes        0.9159      0.651      1.406      0.160      -0.360       2.192\n",
       "Itching_Yes               -2.8029      0.673     -4.167      0.000      -4.121      -1.485\n",
       "Irritability_Yes           2.3407      0.591      3.964      0.000       1.183       3.498\n",
       "delayed healing_Yes       -0.3916      0.550     -0.712      0.476      -1.470       0.686\n",
       "partial paresis_Yes        1.1593      0.525      2.209      0.027       0.131       2.188\n",
       "muscle stiffness_Yes      -0.7288      0.580     -1.256      0.209      -1.866       0.408\n",
       "Alopecia_Yes               0.1504      0.620      0.242      0.808      -1.065       1.366\n",
       "Obesity_Yes               -0.2890      0.544     -0.531      0.595      -1.356       0.778\n",
       "==========================================================================================\n",
       "\n",
       "Possibly complete quasi-separation: A fraction 0.24 of observations can be\n",
       "perfectly predicted. This might indicate that there is complete\n",
       "quasi-separation. In this case some parameters will not be identified.\n",
       "\"\"\""
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "x_constant=sm.add_constant(x)\n",
    "log_reg=sm.Logit(y,x_constant).fit()\n",
    "log_reg.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.naive_bayes import GaussianNB\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn.ensemble import GradientBoostingClassifier,RandomForestClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [],
   "source": [
    "BE_NB=[]\n",
    "VE_NB=[]\n",
    "NB=GaussianNB()\n",
    "Kfold=KFold(shuffle=True,n_splits=3,random_state=0)\n",
    "score=cross_val_score(NB,x,y,cv=Kfold,scoring='roc_auc')\n",
    "BE_NB=np.mean(1-score)\n",
    "VE_NB=np.std(score,ddof=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bias error 0.04314798460846562 Var error 0.013504932962844619 score 0.9568520153915344\n"
     ]
    }
   ],
   "source": [
    "print('bias error',BE_NB,'Var error',VE_NB,'score',np.mean(score))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [],
   "source": [
    "BE_KNN=[]\n",
    "VE_KNN=[]\n",
    "for i in range(3,15):\n",
    "    KNN=KNeighborsClassifier(n_neighbors=i)\n",
    "    Kfold=KFold(shuffle=True,n_splits=3,random_state=0)\n",
    "    score=cross_val_score(KNN,x,y,cv=Kfold,scoring='roc_auc')\n",
    "    BE_KNN=np.mean(1-score)\n",
    "    VE_KNN=np.std(score,ddof=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "invalid index to scalar variable.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-115-f12b2dbd8339>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'min value of BE'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0margmin\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mBE_KNN\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mBE_KNN\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0margmin\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mBE_KNN\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mVE_KNN\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0margmin\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mBE_KNN\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'min value of VE'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0margmin\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mVE_KNN\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mBE_KNN\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0margmin\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mVE_KNN\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mVE_KNN\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0margmin\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mVE_KNN\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mIndexError\u001b[0m: invalid index to scalar variable."
     ]
    }
   ],
   "source": [
    "print('min value of BE',np.argmin(BE_KNN)+3,BE_KNN[np.argmin(BE_KNN)],VE_KNN[np.argmin(BE_KNN)])\n",
    "print('min value of VE',np.argmin(VE_KNN)+3,BE_KNN[np.argmin(VE_KNN)],VE_KNN[np.argmin(VE_KNN)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {},
   "outputs": [],
   "source": [
    "BE_RF=[]\n",
    "VE_RF=[]\n",
    "for i in range(1,50):\n",
    "    RF=RandomForestClassifier(n_estimators=i,random_state=0)\n",
    "    Kfold=KFold(shuffle=True,n_splits=3,random_state=0)\n",
    "    score=cross_val_score(RF,x,y,cv=Kfold,scoring='roc_auc')\n",
    "    BE_RF.append(np.mean(1-score))\n",
    "    VE_RF.append(np.std(score,ddof=1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "min value of BE 46 0.0010766569199496996 0.001170934205775826 0.9988996561891653\n",
      "min value of VE 47 0.0010766569199497367 0.0011709342057758178 0.9988996561891653\n"
     ]
    }
   ],
   "source": [
    "print('min value of BE',np.argmin(BE_RF),BE_RF[np.argmin(BE_RF)],VE_RF[np.argmin(BE_RF)],np.mean(score))\n",
    "print('min value of VE',np.argmin(VE_RF),BE_RF[np.argmin(VE_RF)],VE_RF[np.argmin(VE_RF)],np.mean(score))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {},
   "outputs": [],
   "source": [
    "RF=RandomForestClassifier(n_estimators=47,random_state=0)\n",
    "Kfold=KFold(shuffle=True,n_splits=3,random_state=0)\n",
    "score=cross_val_score(RF,x,y,cv=Kfold,scoring='roc_auc')\n",
    "BE_RF=np.mean(1-score)\n",
    "VE_RF=np.std(score,ddof=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " BE 0.0010766569199496996 Var_error 0.001170934205775826 0.9989233430800503\n"
     ]
    }
   ],
   "source": [
    "print(' BE',BE_RF,'Var_error',VE_RF,np.mean(score))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [],
   "source": [
    "BE_GB=[]\n",
    "VE_GB=[]\n",
    "for i in range(1,200):\n",
    "    GB=GradientBoostingClassifier(n_estimators=i)\n",
    "    Kfold=KFold(shuffle=True,n_splits=3,random_state=0)\n",
    "    score=cross_val_score(GB,x,y,cv=Kfold,scoring='roc_auc')\n",
    "    BE_GB.append(np.mean(1-score))\n",
    "    VE_GB.append(np.std(score,ddof=1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "min value of BE 86 0.01056185438102338 0.0071740815181880095 0.9875700846850214\n",
      "min value of VE 39 0.01314272856447359 0.006773103739029997 0.9875700846850214\n"
     ]
    }
   ],
   "source": [
    "print('min value of BE',np.argmin(BE_GB),BE_GB[np.argmin(BE_GB)],VE_GB[np.argmin(BE_GB)],np.mean(score))\n",
    "print('min value of VE',np.argmin(VE_GB),BE_GB[np.argmin(VE_GB)],VE_GB[np.argmin(VE_GB)],np.mean(score))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "metadata": {},
   "outputs": [],
   "source": [
    "RF=RandomForestClassifier(n_estimators=47,random_state=0)\n",
    "y_pred=RF.fit(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.99909332, 0.99767671, 1.        ])"
      ]
     },
     "execution_count": 169,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "metadata": {},
   "outputs": [],
   "source": [
    "pickle.dump(y_pred,open('model.pkl','wb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "metadata": {},
   "outputs": [],
   "source": [
    "model=pickle.load(open('model.pkl','rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Age', 'Gender_Male', 'Polyuria_Yes', 'Polydipsia_Yes',\n",
       "       'sudden weight loss_Yes', 'weakness_Yes', 'Polyphagia_Yes',\n",
       "       'Genital thrush_Yes', 'visual blurring_Yes', 'Itching_Yes',\n",
       "       'Irritability_Yes', 'delayed healing_Yes', 'partial paresis_Yes',\n",
       "       'muscle stiffness_Yes', 'Alopecia_Yes', 'Obesity_Yes'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 156,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender_Male</th>\n",
       "      <th>Polyuria_Yes</th>\n",
       "      <th>Polydipsia_Yes</th>\n",
       "      <th>sudden weight loss_Yes</th>\n",
       "      <th>weakness_Yes</th>\n",
       "      <th>Polyphagia_Yes</th>\n",
       "      <th>Genital thrush_Yes</th>\n",
       "      <th>visual blurring_Yes</th>\n",
       "      <th>Itching_Yes</th>\n",
       "      <th>Irritability_Yes</th>\n",
       "      <th>delayed healing_Yes</th>\n",
       "      <th>partial paresis_Yes</th>\n",
       "      <th>muscle stiffness_Yes</th>\n",
       "      <th>Alopecia_Yes</th>\n",
       "      <th>Obesity_Yes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>58</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>41</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>45</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>60</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Age  Gender_Male  Polyuria_Yes  Polydipsia_Yes  sudden weight loss_Yes  \\\n",
       "0   40            1             0               1                       0   \n",
       "1   58            1             0               0                       0   \n",
       "2   41            1             1               0                       0   \n",
       "3   45            1             0               0                       1   \n",
       "4   60            1             1               1                       1   \n",
       "\n",
       "   weakness_Yes  Polyphagia_Yes  Genital thrush_Yes  visual blurring_Yes  \\\n",
       "0             1               0                   0                    0   \n",
       "1             1               0                   0                    1   \n",
       "2             1               1                   0                    0   \n",
       "3             1               1                   1                    0   \n",
       "4             1               1                   0                    1   \n",
       "\n",
       "   Itching_Yes  Irritability_Yes  delayed healing_Yes  partial paresis_Yes  \\\n",
       "0            1                 0                    1                    0   \n",
       "1            0                 0                    0                    1   \n",
       "2            1                 0                    1                    0   \n",
       "3            1                 0                    1                    0   \n",
       "4            1                 1                    1                    1   \n",
       "\n",
       "   muscle stiffness_Yes  Alopecia_Yes  Obesity_Yes  \n",
       "0                     1             1            1  \n",
       "1                     0             1            0  \n",
       "2                     1             1            0  \n",
       "3                     0             0            0  \n",
       "4                     1             1            1  "
      ]
     },
     "execution_count": 157,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "metadata": {},
   "outputs": [],
   "source": [
    "x1=x.copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=x.rename(columns={'sudden weight loss_Yes':'sudden_weight_loss_Yes','Genital thrush_Yes':'Genital_thrush_Yes',\n",
    "                    'visual blurring_Yes':'visual_blurring_Yes','delayed healing_Yes':'delayed_healing_Yes',\n",
    "                   'partial paresis_Yes':'partial_paresis_Yes','muscle stiffness_Yes':'muscle_stiffness_Yes'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender_Male</th>\n",
       "      <th>Polyuria_Yes</th>\n",
       "      <th>Polydipsia_Yes</th>\n",
       "      <th>sudden_weight_loss_Yes</th>\n",
       "      <th>weakness_Yes</th>\n",
       "      <th>Polyphagia_Yes</th>\n",
       "      <th>Genital_thrush_Yes</th>\n",
       "      <th>visual_blurring_Yes</th>\n",
       "      <th>Itching_Yes</th>\n",
       "      <th>Irritability_Yes</th>\n",
       "      <th>delayed_healing_Yes</th>\n",
       "      <th>partial_paresis_Yes</th>\n",
       "      <th>muscle_stiffness_Yes</th>\n",
       "      <th>Alopecia_Yes</th>\n",
       "      <th>Obesity_Yes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>58</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>41</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>45</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>60</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Age  Gender_Male  Polyuria_Yes  Polydipsia_Yes  sudden_weight_loss_Yes  \\\n",
       "0   40            1             0               1                       0   \n",
       "1   58            1             0               0                       0   \n",
       "2   41            1             1               0                       0   \n",
       "3   45            1             0               0                       1   \n",
       "4   60            1             1               1                       1   \n",
       "\n",
       "   weakness_Yes  Polyphagia_Yes  Genital_thrush_Yes  visual_blurring_Yes  \\\n",
       "0             1               0                   0                    0   \n",
       "1             1               0                   0                    1   \n",
       "2             1               1                   0                    0   \n",
       "3             1               1                   1                    0   \n",
       "4             1               1                   0                    1   \n",
       "\n",
       "   Itching_Yes  Irritability_Yes  delayed_healing_Yes  partial_paresis_Yes  \\\n",
       "0            1                 0                    1                    0   \n",
       "1            0                 0                    0                    1   \n",
       "2            1                 0                    1                    0   \n",
       "3            1                 0                    1                    0   \n",
       "4            1                 1                    1                    1   \n",
       "\n",
       "   muscle_stiffness_Yes  Alopecia_Yes  Obesity_Yes  \n",
       "0                     1             1            1  \n",
       "1                     0             1            0  \n",
       "2                     1             1            0  \n",
       "3                     0             0            0  \n",
       "4                     1             1            1  "
      ]
     },
     "execution_count": 167,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
