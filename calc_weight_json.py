import jsonFileHandler
import os

# Specify the correct absolute path to the insulin.json file
file_path = 'C:/Users/Alex/Documents/Per scholas/github folder/githubfolder-PerScholas/insulin.json'

# Debugging: Print the absolute path of the file
print("Absolute path of the file:", os.path.abspath(file_path))

# Check if the file exists
if not os.path.exists(file_path):
    print("File does not exist. Exiting program.")
else:
    data = jsonFileHandler.readJsonFile(file_path)

    if data != "":
        bInsulin = data['molecules']['bInsulin']
        aInsulin = data['molecules']['aInsulin']
        insulin = bInsulin + aInsulin
        molecularWeightInsulinActual = data['molecularWeightInsulinActual']
        print('bInsulin: ' + bInsulin)
        print('aInsulin: ' + aInsulin)
        print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
    else:
        print("Error. Exiting program")
        
# Calculating the molecular weight of insulin  
# Getting a list of the amino acid (AA) weights  
aaWeights = data['weights']
# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  
# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))
print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))