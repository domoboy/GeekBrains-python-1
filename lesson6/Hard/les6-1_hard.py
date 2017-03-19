# lesson6-1, hard
import classes as cl

workers = cl.parse_file('workers.txt', cl.Person_Card)
fact = cl.parse_file('hourse_of.txt', cl.Person_Work)

print(workers[0].get_card)
