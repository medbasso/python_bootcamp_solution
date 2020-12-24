row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

horizanal = int(position[0])
vertical = int(position[1])

select_row = map[vertical - 1] 
select_row[horizanal - 1]= 'X'

print(f"{row1}\n{row2}\n{row3}")