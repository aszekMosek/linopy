from benchmark_pulp import model

n = int(snakemake.wildcards.N)
solver = snakemake.wildcards.solver
model(n, solver)
