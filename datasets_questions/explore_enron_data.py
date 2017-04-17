#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import numpy
import pandas

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
' Guetting the number of peple in the dataset '
data_size = len(enron_data)
print "Size of dataset: " + str(data_size)

'The keys() method returns a LIST of all keys used in the dictionary, in an arbitrary order'
#Keys (Names)
names = enron_data.keys()
print "Keys: \n" + str(names)

'Each key maps to another dictionary'
#feature names
features = enron_data[enron_data.keys()[0]].keys()
print "Features: \n" + str(features)

'Getting the number of features in the dataset'
no_feature = len(features)
print "Number of features: " + str(no_feature)

'return all Pois in the dataset'
pois_in_dataset = [key for key in enron_data.keys() if enron_data[key]["poi"] == 1]

print "Number of POI in the dataset: "+ str(len(pois_in_dataset))

'Total value stock of James Prentice'
print "Total value stock of James Prentice: " + str(enron_data["PRENTICE JAMES"]["total_stock_value"])

'Number of messages from Wesley Colwell to POIs'
print "Number of messages from Wesley Colwell to POIs: " + str(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

'Value stock options exercised by Jeff Skilling'
print "Value stock options exercised by Jeff Skilling: " + str(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

##### Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of “total_payments” feature)? 
##### How much money did that person get?
execs = [s for s in enron_data.keys() if ("SKILLING" in s) or ("LAY" in s) or ("FASTOW" in s) ] 
print "Who took the most money: "+str(max( [(enron_data[person]['total_payments'],person) for person in execs]))

#Quantified Salaries
quantified_salaries = [key for key in enron_data.keys() if numpy.isnan(float(enron_data[key]["salary"])) != True]
print "Quantified Salaries: " + str(len(quantified_salaries))

#Know E-mail adressess
known_email_adresses =  [key for key in enron_data.keys() if (enron_data[key]["email_address"]) != 'NaN']
print "Known E-mail Addresses: " + str(len(known_email_adresses))

#Percentage of people with NaN in total payments
total_payments_nan =  [key for key in enron_data.keys() if (enron_data[key]["total_payments"]) == 'NaN']
print "Percentage of NaN in total_payments: " + str((len(total_payments_nan)/float(data_size)) *100)

#Percentage of POIs with NaN in total payments
pois_total_payments_nan =  [key for key in pois_in_dataset if enron_data[key]["total_payments"] == 'NaN']
print "Percentage of POIs NaN in total_payments: " + str((len(pois_total_payments_nan)/float(data_size)) *100)
