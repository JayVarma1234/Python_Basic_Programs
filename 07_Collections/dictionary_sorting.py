marks={'ABC':70,'EFG':50,'HIJ':60,'XYZ':80}
asc = dict(sorted(marks.items(),key=lambda items:items[1]))
print("ascending:",asc)
desc = dict(sorted(marks.items(),key=lambda items:items[1],reverse=True))
print("descending:",desc)
