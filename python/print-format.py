name = "sars_cov_2"
disease = "covid_19"

print(f"The virus {name} causes the disease {disease}.")
print("The virus {} causes the disease {}.".format(name, disease))
print("The virus %s causes the disease %s." % (name, disease))
print("The virus " + name + " causes the disease " + disease + ".")
print("The virus {v} causes the disease {d}.".format(v=name, d=disease))
print("The virus {1} causes the disease {0}.".format(name, disease))
print("The virus {name} causes the disease {disease}.".format(name=name, disease=disease))
