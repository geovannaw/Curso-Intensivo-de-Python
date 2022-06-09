from models import show_completed_models,models

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
models(unprinted_designs, completed_models)
show_completed_models(completed_models)