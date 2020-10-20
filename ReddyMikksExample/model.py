import pyomo.environ as pyo

model = pyo.ConcreteModel()

model.x = pyo.Var([1, 2], domain=pyo.NonNegativeReals)

model.OBJ = pyo.Objective(expr=5 * model.x[1] + 4 * model.x[2], sense=pyo.maximize)

model.Constraint1 = pyo.Constraint(expr=6 * model.x[1] + 4 * model.x[2] <= 24)
model.Constraint2 = pyo.Constraint(expr=model.x[1] + 2 * model.x[2] <= 6)
model.Constraint3 = pyo.Constraint(expr=-model.x[1] + model.x[2] <= 1)
model.Constraint4 = pyo.Constraint(expr=model.x[2] <= 2)
