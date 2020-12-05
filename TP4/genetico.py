import random
import hill

def random_selection(poblacion, ft_objetivo):
	monto_actual = 0
	fitness_total = []
	for i in range(len(poblacion)):
		monto_actual += fitness(poblacion[i], ft_objetivo)
		fitness_total.append(monto_actual)
	prob = random.uniform(0, fitness_total[-1])
	for i in range(len(poblacion)):
		if fitness_total[i] > prob:
			return poblacion[i]

def mutacion(hijo):
	return intercambio(1, hijo)

def reproduccion(x):
	return intercambio(2, x)


def calcula_ft_objetivo(n):
	ft_objetivo = 0
	for i in range(n):
		ft_objetivo += i
	return ft_objetivo

def intercambio(n, objetivo):
	for i in range(n):
		n = random.randint(0, len(objetivo)-1)
		m = random.randint(0, len(objetivo)-1)
		objetivo[n], objetivo[m] = objetivo[m], objetivo[n]
	return objetivo


def algoritmo_genetico(poblacion):
	cont= 100000
	ft_objetivo = calcula_ft_objetivo(len(random.choice(poblacion)))
	while cont > 0: 
		nuevaPoblacion = []
		for i in range(len(poblacion)):
			x = random_selection(poblacion, ft_objetivo)
			hijo = reproduccion(x)
			if random.uniform(0,1) < 1.0:
				hijo = mutacion(hijo)
			if fitness(hijo, ft_objetivo) >= ft_objetivo:
				return hijo
			nuevaPoblacion.append(hijo)
		poblacion = nuevaPoblacion	
		cont -= 1
	return hijo

def fitness(individuo, ft_objetivo):
	valor_ft = ft_objetivo
	for i in range(len(individuo)):
		j = 1
		while j < len(individuo)-i:
			if (individuo[i] == individuo[i+j]+j) or (individuo[i] == individuo[i+j]-j):
				valor_ft -= 1
			j += 1
	return valor_ft