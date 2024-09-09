data_frame.shape()
data_frame=pd.read_csv('data.csv')
data_frame.shape
data_frame=pd.read_csv('FIFA19.csv')
data_frame.shape
data_frame.describe()

data_frame.values
array([[0, 'L. Messi', 31, ..., '€226.5M', 'LALIGA SANTANDER',
        'Complete Forward'],
       [1, 'Cristiano Ronaldo', 33, ..., '€127.1M', 'SERIE A TIM',
        'Distance Shooter'],
       [2, 'Neymar Jr', 26, ..., '€228.1M', 'LIGUE 1 CONFORAMA',
        'Complete Forward'],
       ...,
       [18204, 'B. Worman', 16, ..., '€165K', '0', 'No Speciality'],
       [18205, 'D. Walker-Rice', 17, ..., '€143K', 'EFL LEAGUE TWO',
        'No Speciality'],
       [18206, 'G. Nugent', 16, ..., '€165K', 'EFL LEAGUE TWO',
        'No Speciality']], dtype=object)
data_frame[data_frame['Age']>40].head()
data_frame['Age']>40
df1= pd.DataFrame(data_frame, columns=['Name','Wage','Value'])
def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    return 0.0
wage=df1['']
df['difference'] = df1['Value']-df1['Wage']
df1.sort_values('difference', ascending=True)
import seaborn
import seaborn as sns
 sns.set()
 graph=sns.scatterplot(x='Wage', y='Value', data=df1)
from bokeh.plotting import figure, show
from bokeh.models import HoverTool
from bokeh.plotting import figure, show
from bokeh.models import HoverTool

                                    #########app no. 2 #############


from sklearn.datasets import load_iris
iris = load_iris()
iris.target
type(X)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.4)
