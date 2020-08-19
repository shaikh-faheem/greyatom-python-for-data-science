# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
bank = pd.read_csv(path)
print(bank)

print("="*20)
# code starts here
categorical_var =  bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)


# code ends here


# --------------
# code starts here
banks = bank.drop('Loan_ID',axis=1)
# print(banks)
print(banks.isnull().sum())

bank_mode = banks.mode()
print(bank_mode)

banks = banks.fillna(value = 'bank_mode' )
print(banks)

#code ends here   


# --------------
# code starts here

# check the avg_loan_amount

avg_loan_amount = banks.pivot_table(values=["LoanAmount"], index=["Gender","Married","Self_Employed"], aggfunc=np.mean)


print (avg_loan_amount)
# code ends here,  


# --------------
# code starts here

loan_approved_se = banks[(banks['Self_Employed']== 'Yes') & (banks['Loan_Status']== 'Y')].Self_Employed.count()
print(loan_approved_se)

loan_approved_nse = banks[(banks['Self_Employed']== 'No') & (banks['Loan_Status']== 'Y')].Self_Employed.count()
print(loan_approved_nse)



percentage_se = (loan_approved_se * 100 / 614)

percentage_nse = (loan_approved_nse * 100 / 614)

print(percentage_nse)



# code ends here


# --------------
# code starts here


loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)


print(loan_term)


big_loan_term = banks[loan_term>=25].Loan_Amount_Term.count()

print(big_loan_term)

# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby("Loan_Status")

loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
print(loan_groupby)

mean_values = loan_groupby.mean()
print(mean_values)

# code ends here




