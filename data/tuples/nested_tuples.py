def steps():
  likelihoods = [("Step 1",50),("Step 2",38),("Step 3 ", 27),("Step 4 ", 99),("Step 5 ", 4 )]
  return likelihoods

def run():
  propabilities = steps()
  good_steps = []
  bad_steps = []
  for tuplex in propabilities:
    if tuplex[1]>=50:
      bad_steps.append(tuplex)
    else:
      good_steps.append(tuplex)
  print("Good steps: {}, Bad steps : {}".format(len(good_steps),len(bad_steps)))

run()
