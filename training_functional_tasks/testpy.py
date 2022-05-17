# оставить только те, которые начинаются с 4 или буквы с
days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']

res = sorted(list(filter(lambda x: x if len(x) == 4 or x[0] == "S" else None, days)))
print(*res, sep = '\n' )