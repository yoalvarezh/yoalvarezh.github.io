import pandas as pd

data = [[45939, 21574, 2876, 1815, 1646],
        [60423, 29990, 4708, 2568, 2366],
        [64721, 32510, 5230, 2695, 2526],
        [68484, 35218, 6662, 2845, 2691],
        [71799, 37598, 6856, 3000, 2868]]



data = pd.DataFrame(
    data = data,
    index = [1951, 1956, 1957, 1958, 1959],
    columns = ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena']
)


for col in data.columns:
    fig = data.plot.bar(y=col).get_figure().savefig('figs/' + col + '.png')




from jinja2 import Template

str = open('templates/resultados_template.html', 'r').read()
template = Template(str)
str = template.render(regions=data.columns.tolist())
open('resultados.html', 'w').write(str);