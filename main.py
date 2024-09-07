
import csv

def open_file():
    final = {}
    with open('input.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        d = next(reader, None) 
        agent_col = ask_which_col(d, "Which column is agent names?")
        #queue_col = ask_which_col(d, "Which column is queue names?")
        wrap_col = ask_which_col(d, "Which column is wrap ups?")

        for row in reader:
            agent_list = row[agent_col].split(";")
            #queue_list = row[queue_col].split(",")
            wrap_list = row[wrap_col].split(";")
            for i, agent in enumerate(agent_list):
                agent = agent.strip()
                if agent not in final:
                    final[agent] = {
                        "wrap_ups": [],
                        "total": 0
                    }
                wrap_up = wrap_list[i].strip()
                if not wrap_up in final[agent]["wrap_ups"]:
                    final[agent]["wrap_ups"].append(wrap_up)
                final[agent]["total"] += 1

    print(final)
    return final

def ask_which_col(header, question):
    for i, v in enumerate(header):
        print(f"{i} : {v}")
    return int(input("{} (ie: 0) ".format(question)))

def write_file(final):
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        header = ["Name", "Wrap Up Code", "Count"]
        writer.writerow(header)
        for agent, data in final.items():
            writer.writerow([agent, ', '.join(data['wrap_ups']), data["total"]])


final = open_file()
write_file(final)
